# Jawabdeh (जवाबदेह)

**Who is actually responsible for this problem, and how do I get it fixed?**

An open dataset and a tiny app for Indian cities. Pick your city, pick the problem (pothole, no water, garbage, streetlight…), and it tells you:

1. Which department is responsible (not just "your MLA")
2. The official channel to complain on, with phone numbers and portals
3. The escalation ladder if nothing happens: zone office → councillor → state grievance system → MLA/MP → RTI
4. A ready-to-send complaint draft in Hindi or English

**30 cities across 17 states**, chosen from tier-2 India where good civic information is hardest to find: Agra, Bhopal, Bhubaneswar, Chandigarh, Coimbatore, Dehradun, Guwahati, Indore, Jabalpur, Jaipur, Jodhpur, Kanpur, Kochi, Lucknow, Ludhiana, Madurai, Mysuru, Nagpur, Nashik, Patna, Raipur, Rajkot, Ranchi, Surat, Thiruvananthapuram, Udaipur, Vadodara, Varanasi, Vijayawada, Visakhapatnam.

Built for NGOs and community workers: works in Hindi and English, the complaint draft can be copied or sent straight to WhatsApp, and "Share this guide" copies a short summary for a WhatsApp group.

## Why not just "find your MP"?

That already exists (PRS, MyNeta). And most daily problems are not an MP's or MLA's job. A pothole on a city road belongs to the municipal engineering department, and the fastest fix is a complaint to them with a reference number. Representatives are the escalation step, not the first stop.

## Principles

- **The data is the product.** Everything lives in plain JSON in `data/`, so anyone can fork it, build a better app on it, or keep it alive.
- **Every fact carries its source** and a `status`: `verified` or `needs_verification`. Never present a guess as fact.
- **Official channels only.** No personal phone numbers of officials or representatives, ever. Office lines, helplines and portals only.
- **No tracking.** The app runs fully in the browser: no accounts, no analytics, nothing about the user leaves their phone.
- **Neutral.** Party names are listed as public record. No ratings, no commentary on individuals.

## Repo layout

```
data/
  problems.json        # problem types → responsible body, escalation ladder (generic)
  national.json        # channels that work everywhere (112, CPGRAMS, 1912, RTI…)
  states.json          # state grievance system + channels shared by all cities in a state
  cities/<city>.json   # municipal channels, utilities, MPs/MLAs, coordinates
app/
  template.html        # the app source
  index.html           # built, self-contained app (data inlined)
scripts/
  build.py             # inlines data/ into app/index.html
  seed_data.py         # one-time seed with a source for every entry (kept as a record)
```

## City file schema (short)

| Field | Meaning |
|---|---|
| `state` | Key into `states.json` (state grievance portal, state-wide municipal helplines) |
| `municipal.channels[]` | `type` (phone/web/app/in_person), bilingual label, `value`, `status`, `source` |
| `municipal.escalation` | Written escalation address (grievance cell) |
| `water`, `dev_authority` | Optional: separate water board or development authority |
| `discom` | Electricity distribution company name |
| `reps` | `mps[]`, `mlas[]` (city segments only), `mla_status`, `mla_source`, optional note |
| `geo` | `[lat, lon]`, used to place the city in the 3D view |
| `last_reviewed` | Date someone last checked this file |

## Add your city

1. Copy `data/cities/indore.json` to `data/cities/<your-city>.json`. If the state is new, add it to `data/states.json`.
2. Fill in what you can verify. Put the source URL on every line. Mark anything uncertain `needs_verification`.
3. Run `python3 scripts/build.py` and open `app/index.html` to check.
4. Open a pull request.

The most valuable contributions right now: **ward councillor lists**, **ward → assembly constituency mapping**, verified helplines for Ludhiana, Jodhpur, Udaipur and Coimbatore, and MLA names for Coimbatore and Madurai (elected May 2026). Note: the 2008 delimitation orders use old ward numbers that no longer match current wards, so they cannot be copied directly.

## Licence

- Code: MIT
- Data: CC BY 4.0. Please credit "Jawabdeh contributors" and keep sources attached.

## Maintainer

Built and maintained by Dabeer Ul Haq. Corrections and new cities are welcome: see CONTRIBUTING.md.

## Disclaimer

Jawabdeh is a directory and a letter template. Each complaint belongs to the person who files it. The project takes no position on any party or official.

Phone numbers and officeholders change. Check the `status` and `last_reviewed` fields, and in an emergency always call **112** first.
