import streamlit as st
import pandas as pd
from nba_data import get_player_id, get_player_stats
import altair as alt

st.set_page_config(page_title="NBA Head-to-Head", page_icon="🏀")
st.title("🏀 NBA Head-to-Head Player Comparison")

# --- Player 1 ---
player_1 = st.text_input("🔎 Player 1 Full Name", key="player_1")
player_2 = st.text_input("🆚 Player 2 Full Name", key="player_2")

stats_1 = None
stats_2 = None
season_selected = None

if player_1 and player_2:
    player_1_id = get_player_id(player_1)
    player_2_id = get_player_id(player_2)

    if player_1_id and player_2_id:
        stats_1 = get_player_stats(player_1_id)
        stats_2 = get_player_stats(player_2_id)

        common_seasons = sorted(
            list(set(stats_1["SEASON_ID"]).intersection(set(stats_2["SEASON_ID"]))), reverse=True
        )

        if common_seasons:
            season_selected = st.selectbox("📅 Select Season", common_seasons)

            df_1 = stats_1[stats_1["SEASON_ID"] == season_selected]
            df_2 = stats_2[stats_2["SEASON_ID"] == season_selected]

            st.subheader(f"📊 {player_1} vs {player_2} - {season_selected}")
            combined = pd.DataFrame({
                "Stat": ["PTS", "AST", "REB", "STL", "BLK"],
                player_1: [
                    float(df_1["PTS"].values[0]),
                    float(df_1["AST"].values[0]),
                    float(df_1["REB"].values[0]),
                    float(df_1["STL"].values[0]),
                    float(df_1["BLK"].values[0]),
                ],
                player_2: [
                    float(df_2["PTS"].values[0]),
                    float(df_2["AST"].values[0]),
                    float(df_2["REB"].values[0]),
                    float(df_2["STL"].values[0]),
                    float(df_2["BLK"].values[0]),
                ],
            })

            chart_data = combined.melt("Stat", var_name="Player", value_name="Value")

            chart = alt.Chart(chart_data).mark_bar().encode(
                x="Stat:N",
                y="Value:Q",
                color="Player:N",
                tooltip=["Player", "Stat", "Value"]
            ).properties(width=600, height=400)

            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("These players do not have overlapping seasons.")
    else:
        st.error("One or both players not found.")
