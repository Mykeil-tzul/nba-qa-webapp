import streamlit as st
import openai
from nba_data import get_player_id, get_player_stats

# Set page config
st.set_page_config(page_title="NBA Player Stats Q&A", page_icon="🏀")
st.title("🏀 NBA Player Stats Q&A App")

# 🔐 Load OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Player 1 Section ---
st.subheader("🔎 Player 1")
player_1 = st.text_input("Enter Player 1 Full Name (e.g., LeBron James)", key="player_1")
stats_1 = None
selected_season_1 = None

if player_1:
    player_1_id = get_player_id(player_1)
    if player_1_id:
        stats_1 = get_player_stats(player_1_id)
        if stats_1 is not None and not stats_1.empty:
            seasons_1 = stats_1["SEASON_ID"].unique().tolist()[::-1]
            selected_season_1 = st.selectbox(f"Select Season for {player_1}", seasons_1, key="season_1")
            st.write(f"📊 Stats for {player_1} in {selected_season_1}")
            st.dataframe(stats_1[stats_1["SEASON_ID"] == selected_season_1].reset_index(drop=True))
        else:
            st.warning(f"No stats found for {player_1}")
    else:
        st.error(f"Player {player_1} not found.")

# --- Player 2 Section ---
st.subheader("🆚 Compare With Another Player (Optional)")
player_2 = st.text_input("Enter Player 2 Full Name (e.g., Kevin Durant)", key="player_2")
stats_2 = None
selected_season_2 = None

if player_2:
    player_2_id = get_player_id(player_2)
    if player_2_id:
        stats_2 = get_player_stats(player_2_id)
        if stats_2 is not None and not stats_2.empty:
            seasons_2 = stats_2["SEASON_ID"].unique().tolist()[::-1]
            selected_season_2 = st.selectbox(f"Select Season for {player_2}", seasons_2, key="season_2")
            st.write(f"📊 Stats for {player_2} in {selected_season_2}")
            st.dataframe(stats_2[stats_2["SEASON_ID"] == selected_season_2].reset_index(drop=True))
        else:
            st.warning(f"No stats found for {player_2}")
    else:
        st.error(f"Player {player_2} not found.")

# --- OpenAI Chat Section ---
st.subheader("💬 Ask the AI About NBA Players")
st.caption("Ask a question like 'Who had more assists in 2023?' or 'Compare LeBron and Durant:'")
user_question = st.text_input("Your question:")

if user_question:
    with st.spinner("🤖 Thinking..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_question}],
                temperature=0.7,
                max_tokens=150
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"OpenAI Error: {e}")
