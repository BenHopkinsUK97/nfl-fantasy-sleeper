import requests
import pandas as pd

BASE_URL = "https://api.sleeper.app/v1"
LEAGUE_ID = "1312090981205577728"


def get_rosters(league_id: str) -> pd.DataFrame:
    """Fetch all rosters for the league and explode to one row per player."""
    url = f"{BASE_URL}/league/{league_id}/rosters"
    data = requests.get(url).json()
    df = pd.json_normalize(data)
    df = df.explode("players")
    df = df.rename(columns={
        "settings.wins": "wins",
        "settings.losses": "losses",
        "settings.ties": "ties",
        "metadata.team_name": "team_name",
    })
    return df


def get_users(league_id: str) -> pd.DataFrame:
    """Fetch all users (managers) in the league."""
    url = f"{BASE_URL}/league/{league_id}/users"
    users = requests.get(url).json()
    return pd.json_normalize(users)


def get_players() -> pd.DataFrame:
    """Fetch the full NFL player database from Sleeper."""
    url = f"{BASE_URL}/players/nfl"
    players = requests.get(url).json()
    return pd.json_normalize(list(players.values()))


def build_master(rosters_df, users_df, players_df) -> pd.DataFrame:
    """Merge rosters → users → players into a single master table."""
    rosters_users = rosters_df.merge(
        users_df,
        left_on="owner_id",
        right_on="user_id",
        how="left",
    )
    master = rosters_users.merge(
        players_df,
        left_on="players",
        right_on="player_id",
        how="left",
    )
    return master


def main():
    print("Fetching rosters...")
    rosters_df = get_rosters(LEAGUE_ID)
    rosters_df.to_csv("sleeper_rosters.csv", index=False)

    print("Fetching users...")
    users_df = get_users(LEAGUE_ID)
    users_df.to_csv("sleeper_users.csv", index=False)

    print("Fetching NFL player database (this may take a moment)...")
    players_df = get_players()
    players_df.to_csv("sleeper_players.csv", index=False)

    print("Building master table...")
    master = build_master(rosters_df, users_df, players_df)
    master.to_csv("sleeper_master.csv", index=False)

    print(f"Done! Master table written: {len(master)} rows, {len(master.columns)} columns.")


if __name__ == "__main__":
    main()
