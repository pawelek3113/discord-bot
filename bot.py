from nextcord.ext import commands
from nextcord import Intents
from dotenv import load_dotenv
import os

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=Intents.all())
        for file in os.listdir("./modules"):
            if file.endswith(".py"):
                self.load_extension(f"modules.{file[:-3]}")

    async def on_ready(self):
        print(f"Logged in as {self.user}")


bot = Bot()
bot.run(os.environ["TOKEN"])
