# Contributing

Jawabdeh is only as good as its numbers. Corrections from people on the ground are the most valuable thing you can give.

## No coding needed

Open an issue using **Report wrong or missing information**. Tell us the city, what is wrong, and how you know (you called it, or it is on an official site). That's it.

## Editing the data directly

1. Edit the JSON in `data/cities/<city>.json` (or `data/states.json` for state-wide channels).
2. Every phone number or link needs a `source` URL and a `status`:
   - `verified`: official government source, or you called it and it worked
   - `needs_verification`: from news, directories or community sites
3. Run `python3 scripts/validate.py` and `python3 scripts/build.py`.
4. Open a pull request. Checks run automatically.

## Rules

- **Office numbers only.** Never add a personal phone number of an official or a representative.
- **No opinions** about officials or parties.
- **Neutral wording** in complaint templates: describe the problem, never a person.

## Most needed now

- Ward councillor lists for any city
- Verified municipal helplines for Ludhiana, Jodhpur, Udaipur, Coimbatore and Mysuru
- MLAs for Coimbatore and Madurai (elected May 2026)
- New cities
