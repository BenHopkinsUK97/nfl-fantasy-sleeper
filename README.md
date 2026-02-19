# NFL Fantasy League Data Pipeline

Side project — nothing to do with finance. Just what happens when you take fantasy football too seriously.

## What it does
Pulls data from the Sleeper Fantasy API and merges it into a single clean CSV. No manual exports, no copy-pasting from the app.

Fetches four sources and combines them into one master table:
- Rosters (players + team records)
- League managers
- Full NFL player database
- Merged output → `sleeper_master.csv`

## Usage
Set your league ID in `sleeper_import.py`:
```python
LEAGUE_ID = "your_league_id_here"
```
Then run:
```bash
python sleeper_import.py
```

## Planned
- Filter by team so you can pull stats for just your roster
- Currently doing this manually in Excel, moving it into the script

## Notes
- The `/players/nfl` fetch can take a few seconds (~10k records)
- CSVs are excluded from version control via `.gitignore`
- Built mainly to get better at pandas, and because manual exports are painful
