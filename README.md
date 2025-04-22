# 🏀 NBA Q&A Web App

A sleek, interactive NBA player stats explorer built with **Streamlit**, **nba_api**, and **OpenAI GPT-3.5**.

This web app allows anyone—from casual fans to data pros—to:
- 🔍 Search for any NBA player
- 📊 View season-by-season stats
- 🆚 Compare two players side-by-side
- 🤖 Ask any basketball-related question (e.g. "Who had more assists in 2023?")

🎯 **Live App** → (https://mt-nba-app-webapp.streamlit.app)

---

## 🚀 Features

- 🔎 **Search Players:** By full name (e.g., "LeBron James")
- 📆 **Filter by Season:** View any season’s stats going back to their rookie year
- 🆚 **Compare Players:** Select a second player and compare both
- 🤖 **AI Assistant:** Ask questions powered by OpenAI’s GPT-3.5
- 💡 Uses official NBA stats from [nba_api](https://github.com/swar/nba_api)

---

## 🛠️ Tech Stack

| Tool            | Use Case                                |
|-----------------|------------------------------------------|
| Streamlit       | Web app framework                        |
| nba_api         | NBA stats and player data                |
| OpenAI GPT-3.5  | Natural language Q&A                     |
| Python          | Backend and data handling                |
| dotenv + secrets.toml | Secure API key management         |

---

## 📦 Setup Locally

```bash
# Clone repo
git clone https://github.com/Mykeil-tzul/nba-qa-webapp.git
cd nba-qa-webapp

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

