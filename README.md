<div align="center">

![MrPikchu-Welcome-Bot](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=MrPikchu-Welcome-Bot&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Welcome+and+Goodbye+Bot+for+Discord&descAlignY=52&descSize=16)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.x-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-2ECC71?style=for-the-badge)](LICENSE)

> A lightweight Discord bot that greets new members with a rich green embed and sends a farewell red embed when someone leaves.

</div>

---

## Features

- Rich **welcome embed** (green) with member avatar, member count and account age
- Rich **goodbye embed** (red) with member avatar and updated member count
- Fully configurable via `config.json` — no code editing needed
- `/testwelcome` and `/testgoodbye` slash commands — restricted to a configurable role
- Clean structured logging to console

---

## Requirements

| | |
|---|---|
| Python | 3.11+ |
| discord.py | 2.x |
| python-dotenv | latest |
| aiohttp | latest |

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mrpikchu/MrPikchu-Welcome-Bot.git
   cd MrPikchu-Welcome-Bot
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create your `.env` file**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in your bot token and client ID.

4. **Enable the Members Intent** in the [Discord Developer Portal](https://discord.com/developers/applications):
   - Go to your application → Bot → Privileged Gateway Intents
   - Enable **Server Members Intent**

5. **Configure `config.json`** — see Configuration section below.

6. **Run the bot**
   ```bash
   python main.py
   ```

---

## Commands

| Command | Description | Requirements |
|---|---|---|
| `/testwelcome` | Preview the welcome embed (ephemeral) | Role defined in `config.json` |
| `/testgoodbye` | Preview the goodbye embed (ephemeral) | Role defined in `config.json` |

---

## Configuration

Open `config.json` and set the following values:

| Key | Description |
|---|---|
| `guild_id` | Your server's ID |
| `channels.welcome` | Channel ID for welcome messages |
| `channels.goodbye` | Channel ID for goodbye messages |
| `roles.bot_admin` | Role ID allowed to use test commands |
| `welcome.welcome_title` | Title of the welcome embed |
| `welcome.welcome_description` | Description — supports `{member}` and `{server}` placeholders |
| `welcome.goodbye_title` | Title of the goodbye embed |
| `welcome.goodbye_description` | Description — supports `{member}` and `{server}` placeholders |
| `welcome.banner_url` | Optional image shown at the bottom of embeds |
| `footer.text` | Footer text shown on all embeds |
| `footer.icon_url` | Optional footer icon URL |

---

## Project Structure

```
MrPikchu-Welcome-Bot/
├── main.py
├── .env
├── .env.example
├── config.json
├── requirements.txt
├── README.md
├── cogs/
│   └── welcome.py
└── utils/
    └── embeds.py
```

---

## How to get IDs

Enable **Developer Mode** in Discord settings (Settings → Advanced → Developer Mode), then:
- Right-click your server → **Copy Server ID** → paste as `guild_id`
- Right-click a channel → **Copy Channel ID** → paste as `channels.welcome` / `channels.goodbye`
- Right-click a role in Server Settings → **Copy Role ID** → paste as `roles.bot_admin`

---

<div align="center">

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=80&section=footer)

Made with ☕ by [MrPikchu](https://github.com/mrpikchu) • discord.py 2.x • Python 3.11

</div>
