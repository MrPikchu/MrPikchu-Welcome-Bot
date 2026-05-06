import discord
from discord.ext import commands
import json
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("WelcomeBot")

with open("config.json", "r") as f:
    config = json.load(f)


class WelcomeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)
        self.config = config

    async def setup_hook(self):
        await self.load_extension("cogs.welcome")
        guild = discord.Object(id=self.config["guild_id"])
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        logger.info("Slash commands synced.")

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=self.config["status"],
            )
        )
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")


bot = WelcomeBot()
bot.run(os.getenv("TOKEN"), log_handler=None)