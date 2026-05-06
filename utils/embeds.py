import discord
import json
from datetime import datetime

with open("config.json", "r") as f:
    config = json.load(f)


def _base(title: str, description: str, color: int) -> discord.Embed:
    embed = discord.Embed(title=title, description=description, color=color, timestamp=datetime.utcnow())
    embed.set_footer(
        text=config["footer"]["text"],
        icon_url=config["footer"]["icon_url"] or discord.embeds.EmptyEmbed,
    )
    return embed


def success_embed(title: str, description: str) -> discord.Embed:
    return _base(title, description, config["colors"]["success"])


def error_embed(title: str, description: str) -> discord.Embed:
    return _base(title, description, config["colors"]["error"])


def info_embed(title: str, description: str) -> discord.Embed:
    return _base(title, description, config["colors"]["info"])


def warning_embed(title: str, description: str) -> discord.Embed:
    return _base(title, description, config["colors"]["warning"])


def base_embed(title: str, description: str, color: int) -> discord.Embed:
    return _base(title, description, color)