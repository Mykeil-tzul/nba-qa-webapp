from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# ✅ Step 1: Search player by full name
def get_player_id(player_name):
    try:
        player_dict = players.find_players_by_full_name(player_name)
        if player_dict:
            return player_dict[0]['id']
        return None
    except Exception as e:
        print(f"❌ Error fetching player ID: {e}")
        return None

# ✅ Step 2: Get player career stats
def get_player_stats(player_id):
    try:
        career = playercareerstats.PlayerCareerStats(player_id=player_id)
        return career.get_data_frames()[0]
    except Exception as e:
        print(f"❌ Error fetching player stats: {e}")
        return None

# ✅ Step 3: Run test
if __name__ == "__main__":
    player_name = "LeBron James"
    player_id = get_player_id(player_name)
    print("🎯 Player ID:", player_id)

    if player_id:
        stats_df = get_player_stats(player_id)
        if stats_df is not None:
            print("📊 Latest season stats:")
            print(stats_df.tail(1).to_string(index=False))
        else:
            print("⚠️ No stats found.")
    else:
        print("🚫 Player not found.")










