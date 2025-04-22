from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

def get_player_id(player_name):
    try:
        player_dict = players.find_players_by_full_name(player_name)
        if player_dict:
            return player_dict[0]['id']
        return None
    except Exception as e:
        print(f"❌ Error fetching player ID: {e}")
        return None

def get_player_stats(player_id):
    try:
        career = playercareerstats.PlayerCareerStats(player_id=player_id)
        return career.get_data_frames()[0]
    except Exception as e:
        print(f"❌ Error fetching player stats: {e}")
        return None








