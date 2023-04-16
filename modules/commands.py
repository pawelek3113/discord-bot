import nextcord
import random
from nextcord.ext import commands
import pytz
from datetime import datetime


def utc_to_local(time):
    local_tz = pytz.timezone("Europe/Warsaw")
    local_dt = time.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_dt


def format_time(time: datetime):
    new_time = time.strftime("%H:%M:%S %Z")
    return new_time


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @nextcord.slash_command()
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.send("pong")

    @nextcord.slash_command(name="parrot", guild_ids="1061263631511191632")
    async def test(self, interaction: nextcord.Interaction, msg):
        await interaction.response.send_message(f"{arg}")

    @nextcord.slash_command(name="pick", guild_ids="1061263631511191632")
    async def test2(
        self,
        interaction: nextcord.Interaction,
        number: int = nextcord.SlashOption(choices={"one": 1, "two": 2, "three": 3}),
    ):
        await interaction.response.send_message(f"{number}")

    @nextcord.slash_command(name="hi", guild_ids="1061263631511191632")
    async def test3(self, interaction: nextcord.Interaction, user: nextcord.Member):
        time = interaction.created_at
        local_time = utc_to_local(time)

        await interaction.response.send_message(
            f"{interaction.user.display_name} says hi to {user.mention} in {interaction.channel.mention} at {format_time(local_time)}"
        )

    @nextcord.slash_command(name="slap", guild_ids="1061263631511191632")
    async def test4(self, interaction: nextcord.Interaction):
        members = interaction.guild.members
        user = random.choice(members)
        await interaction.response.send_message(
            f"{interaction.user.display_name} slaps {user.mention} in {interaction.channel.mention}"
        )


def setup(bot):
    bot.add_cog(Commands(bot))
