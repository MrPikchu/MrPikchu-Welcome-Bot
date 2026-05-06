import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import json
import logging

logger = logging.getLogger("WelcomeBot.welcome")

with open("config.json", "r") as f:
    config = json.load(f)


def has_bot_admin_role():
    async def predicate(interaction: discord.Interaction) -> bool:
        role_id = config["roles"]["bot_admin"]
        role = interaction.guild.get_role(role_id)
        if role is None:
            return False
        return role in interaction.user.roles
    return app_commands.check(predicate)


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cfg = config["welcome"]

    def _welcome_embed(self, member: discord.Member) -> discord.Embed:
        embed = discord.Embed(
            title=self.cfg["welcome_title"],
            description=self.cfg["welcome_description"].format(
                member=member.mention,
                server=member.guild.name,
            ),
            color=config["colors"]["success"],
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(
            name=self.cfg["members_field_name"],
            value=f"`{member.guild.member_count}`",
            inline=True,
        )
        embed.add_field(
            name=self.cfg["account_field_name"],
            value=f"<t:{int(member.created_at.timestamp())}:R>",
            inline=True,
        )
        if self.cfg.get("banner_url"):
            embed.set_image(url=self.cfg["banner_url"])
        embed.set_footer(
            text=config["footer"]["text"],
            icon_url=config["footer"]["icon_url"] or None,
        )
        return embed

    def _goodbye_embed(self, member: discord.Member) -> discord.Embed:
        embed = discord.Embed(
            title=self.cfg["goodbye_title"],
            description=self.cfg["goodbye_description"].format(
                member=str(member),
                server=member.guild.name,
            ),
            color=config["colors"]["error"],
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(
            name=self.cfg["members_field_name"],
            value=f"`{member.guild.member_count}`",
            inline=True,
        )
        if self.cfg.get("banner_url"):
            embed.set_image(url=self.cfg["banner_url"])
        embed.set_footer(
            text=config["footer"]["text"],
            icon_url=config["footer"]["icon_url"] or None,
        )
        return embed

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = config["channels"]["welcome"]
        channel = member.guild.get_channel(channel_id)
        if channel is None:
            logger.warning(f"Welcome channel {channel_id} not found.")
            return
        try:
            await channel.send(embed=self._welcome_embed(member))
            logger.info(f"Sent welcome embed for {member} in {channel}.")
        except discord.Forbidden:
            logger.error(f"Missing permissions to send in {channel}.")
        except Exception as e:
            logger.error(f"Unexpected error in on_member_join: {e}")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel_id = config["channels"]["goodbye"]
        channel = member.guild.get_channel(channel_id)
        if channel is None:
            logger.warning(f"Goodbye channel {channel_id} not found.")
            return
        try:
            await channel.send(embed=self._goodbye_embed(member))
            logger.info(f"Sent goodbye embed for {member} in {channel}.")
        except discord.Forbidden:
            logger.error(f"Missing permissions to send in {channel}.")
        except Exception as e:
            logger.error(f"Unexpected error in on_member_remove: {e}")

    @app_commands.command(name="testwelcome", description="Preview the welcome embed (Bot Admin only)")
    @has_bot_admin_role()
    async def test_welcome(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=self._welcome_embed(interaction.user), ephemeral=True)

    @app_commands.command(name="testgoodbye", description="Preview the goodbye embed (Bot Admin only)")
    @has_bot_admin_role()
    async def test_goodbye(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=self._goodbye_embed(interaction.user), ephemeral=True)

    @test_welcome.error
    @test_goodbye.error
    async def on_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        await interaction.response.send_message("❌ You don't have the required role to use this command.", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))