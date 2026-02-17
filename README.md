# NFL Fantasy League Data Pipeline

> **Heads up:** This is a personal side project — nothing to do with finance or quant work.
> Just what happens when i take fantasy league a little too seriously.

---

## What This Does

Pulls live data from the [Sleeper Fantasy Football API](https://docs.sleeper.com/) and stitches it together into a clean, analysis-ready master table. No manual exports, no copy-pasting from the app — just a single script that hands you structured CSVs ready for whatever you want to do next.

The pipeline fetches four data sources and merges them:

| Step | Endpoint | Output |
|------|----------|--------|
| 1 | `/league/{id}/rosters` | One row per rostered player, with team W/L record |
| 2 | `/league/{id}/users` | Manager names and display info |
| 3 | `/players/nfl` | Full NFL player database (name, position, team, etc.) |
| 4 | Merge 1+2+3 | `sleeper_master.csv` — the main event |

---

## In Future i am planning to apply Data cleaning and Filtering for what ever team you would like from your leauge this will likely be within the same Py file ( currently doing all of this in Excel )

## Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/sleeper-nfl-fantasy.git
cd sleeper-nfl-fantasy
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set your league ID**

Open `sleeper_import.py` and update the `LEAGUE_ID` constant at the top:
```python
LEAGUE_ID = "your_league_id_here"
```

> To find your league ID: open Sleeper in a browser, go to your league, and grab the numeric ID from the URL.

**4. Run it**
```bash
python sleeper_import.py
```

You'll get four CSVs in the current directory:

```
sleeper_rosters.csv   — roster data per player
sleeper_users.csv     — league manager info
sleeper_players.csv   — full NFL player database
sleeper_master.csv    — everything merged
```

---

## Project Structure

```
sleeper-nfl-fantasy/
├── sleeper_import.py   # Main pipeline script
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## Tech Stack

- **Python 3.8+**
- [`requests`](https://docs.python-requests.org/) — API calls
- [`pandas`](https://pandas.pydata.org/) — data wrangling and CSV export

## Why This Exists

  Because exporting things manually is unbearable and my dynasty team is pretty poor. Also tyring to learn more around Pandas. 

The Sleeper API is free and doesn't require authentication for public league data, which makes it a clean target for this kind of pipeline.

## Notes

- The `/players/nfl` endpoint returns the full database of NFL players (~10k+ records) so the fetch can take a few seconds.
- The generated CSVs are excluded from version control via `.gitignore` since they contain league-specific data.
- League ID is hardcoded for simplicity.