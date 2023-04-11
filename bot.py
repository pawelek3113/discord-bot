from nextcord.ext import commands
from nextcord import Intents
from dotenv import load_dotenv
import os

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=Intents.all())


bot = Bot()

bot.run(os.environ["TOKEN"])
