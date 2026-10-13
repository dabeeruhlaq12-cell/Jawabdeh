#!/usr/bin/env node
/* No-dependency test: runs the built app's script against a tiny DOM stub and checks that
   nothing ever tells a citizen their complaint is registered unless they recorded a complaint number.
   Run: python3 scripts/build.py && node tests/truthful_status_test.js */
const fs = require('fs'), path = require('path'), assert = require('assert');

const html = fs.readFileSync(path.join(__dirname, '..', 'app', 'index.html'), 'utf8');
const src = html.match(/<script>([\s\S]*?)<\/script>/g).pop().replace(/<\/?script>/g, '');

// --- minimal DOM + browser stubs
const els = {};
const el = id => els[id] || (els[id] = {
  id, innerHTML: '', textContent: '', value: '', hidden: false, dataset: {}, style: {}, href: '', offsetWidth: 1,
  classList: { add() {}, remove() {}, toggle() {} }, focus() {}, select() {}, setAttribute() {},
});
const store = {};
global.document = { getElementById: el, documentElement: {}, addEventListener() {}, querySelector: () => null, createElement: () => el('tmp') };
global.localStorage = { getItem: k => (k in store ? store[k] : null), setItem: (k, v) => { store[k] = String(v); }, removeItem: k => { delete store[k]; } };
global.window = { scrollTo() {}, addEventListener() {} };
global.history = { pushState() {}, replaceState() {}, state: null };

const app = new Function(src + ';return {UI,S,DATA,render,statusKey,statusText,setDraft,loadRefs,storeRefs,latestRef,letterText,waLink};')();
const { S, DATA } = app;

// Words that would claim official registration. The DRAFT stamp and "not submitted" wording are allowed.
const FORBIDDEN = [/\bFILED\b/, /\bregistered\b(?! only)(?!\.)/i, /successfully (sent|submitted|filed)/i, />\s*दर्ज\s*</, /शिकायत दर्ज हो गई/];

let screens = 0;
for (const lang of ['en', 'hi']) {
  for (const c of DATA.cities) {
    for (const p of DATA.problems.problems) {
      Object.assign(S, { lang, city: c.id, prob: p.id, view: 'result', draft: 'draft' });
      app.render();
      const out = els.view.innerHTML;
      assert(!/undefined|NaN|\[object/.test(out), `bad render ${lang}/${c.id}/${p.id}`);
      for (const re of FORBIDDEN) assert(!re.test(out), `misleading text ${re} in ${lang}/${c.id}/${p.id}`);
      // the four steps are present, in order
      const heads = [...out.matchAll(/<h2>(.*?)<\/h2>/g)].map(m => m[1]);
      assert.deepStrictEqual(heads, ['prepH', 'submitH', 'saveH', 'routeH'].map(k => app.UI[lang][k]),
        `steps out of order in ${lang}/${c.id}/${p.id}`);
      assert(out.includes('id="refform"'), 'reference number form missing');
      assert(out.includes('class="truth"'), 'truth notice missing');
      assert(app.statusKey() === 'draft', 'fresh complaint must start as draft');
      screens++;
    }
  }
}

// --- status machine: copying / sharing never reaches "recorded"
Object.assign(S, { lang: 'en', city: 'nagpur', prob: 'road', view: 'result', draft: 'draft' });
app.render();
app.setDraft('copied');
assert.strictEqual(app.statusKey(), 'copied');
assert(/not submitted/i.test(app.statusText()), 'copied status must say not submitted');
app.setDraft('shared');
assert.strictEqual(app.statusKey(), 'shared');
assert(/not with the office/i.test(app.statusText()), 'shared status must say not with the office');
app.setDraft('copied'); // copying again after sharing must not downgrade
assert.strictEqual(app.statusKey(), 'shared');

// --- only a recorded complaint number changes the status, and only for that city + problem
app.storeRefs([{ id: 'x1', city: 'nagpur', prob: 'road', ref: 'NMC/2026/4471', date: '2026-10-13' }]);
assert.strictEqual(app.statusKey(), 'recorded');
assert(app.statusText().includes('NMC/2026/4471'));
S.prob = 'water'; S.draft = 'draft'; // what tapping a new problem does
assert.strictEqual(app.statusKey(), 'draft', 'a number for one problem must not mark another as recorded');
S.prob = 'road'; S.draft = 'shared';
app.render();
assert(els.view.innerHTML.includes('NMC/2026/4471'), 'saved number should show in the escalation step');
app.storeRefs([]);
assert.strictEqual(app.statusKey(), 'shared');

// --- Hindi wording
S.lang = 'hi'; S.draft = 'copied';
assert(/अभी दर्ज नहीं/.test(app.statusText()), 'Hindi copied status must say not registered');

// --- storage failure is handled
const realSet = localStorage.setItem;
localStorage.setItem = () => { throw new Error('blocked'); };
assert.strictEqual(app.storeRefs([{ id: 'y' }]), false, 'storeRefs must report failure');
localStorage.setItem = realSet;

// --- official WhatsApp links go to the office number, with the draft as text
assert(/^https:\/\/wa\.me\/919424401548\?text=/.test(app.waLink('9424401548', 'hi')));

// --- no "FILED" anywhere in the built page
assert(!/\bFILED\b/.test(html), 'built page still contains FILED');

console.log(`ok — ${screens} result screens checked, status rules hold`);
