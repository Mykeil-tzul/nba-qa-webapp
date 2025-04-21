import streamlit as st
from nba_data import get_player_id, get_player_stats

st.set_page_config(page_title="NBA Player Comparison", page_icon="🏀")
st.title("🏀 NBA Player Comparison App")

# Inputs
player_1_name = st.text_input("Enter first player name (e.g., LeBron James):")
player_2_name = st.text_input("Enter second player name (e.g., Stephen Curry):")

# Button
if st.button("Compare Stats"):

    col1, col2 = st.columns(2)

    with col1:
        if player_1_name:
            player_1_id = get_player_id(player_1_name)
            if player_1_id:
                stats_df_1 = get_player_stats(player_1_id)
                if stats_df_1 is not None:
                    seasons_1 = stats_df_1["SEASON_ID"].unique().tolist()
                    selected_season_1 = st.selectbox(f"{player_1_name} - Select Season", seasons_1[::-1])
                    season_stats_1 = stats_df_1[stats_df_1["SEASON_ID"] == selected_season_1]
                    st.subheader(f"📊 {player_1_name} ({selected_season_1})")
                    st.dataframe(season_stats_1.reset_index(drop=True))
                else:
                    st.warning(f"No stats found for {player_1_name}")
            else:
                st.error(f"Player not found: {player_1_name}")

    with col2:
        if player_2_name:
            player_2_id = get_player_id(player_2_name)
            if player_2_id:
                stats_df_2 = get_player_stats(player_2_id)
                if stats_df_2 is not None:
                    seasons_2 = stats_df_2["SEASON_ID"].unique().tolist()
                    selected_season_2 = st.selectbox(f"{player_2_name} - Select Season", seasons_2[::-1])
                    season_stats_2 = stats_df_2[stats_df_2["SEASON_ID"] == selected_season_2]
                    st.subheader(f"📊 {player_2_name} ({selected_season_2})")
                    st.dataframe(season_stats_2.reset_index(drop=True))
                else:
                    st.warning(f"No stats found for {player_2_name}")
            else:
                st.error(f"Player not found: {player_2_name}")


