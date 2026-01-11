from pathlib import Path
from discord.ext import commands
from discord import app_commands
import discord
import logging
import random
import os


logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
pibble_path = BASE_DIR / ".." / ".." / "assets" / "pibble"


class Pibble(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.GIFS = []

        self.files = os.listdir(pibble_path)


    def choose_gif(self):
        index = random.randint(0, len(self.files) - 1)
        return self.files[index]

    @commands.Cog.listener()
    async def on_message(self, message):
        pass
    

    
    @commands.hybrid_command(name="pibble", description="/pibble does something cool.")
    async def pibble(self, ctx):
        ppath = pibble_path.joinpath(self.choose_gif())
        file = discord.File(ppath)
        await ctx.send(file=file)
    
    @commands.hybrid_command(name="pib", description="/pib does something cool.")
    async def pib(self, ctx):
        await ctx.send("I ran pib!")
    
    @commands.hybrid_command(name="washmabelly", description="washmabelly does something cool.")
    async def washmabelly(self, ctx):
        await ctx.send("clean mah bellah!")
    


async def setup(bot: commands.Bot):
    await bot.add_cog(Pibble(bot))

if __name__ == "__main__":
    pib = Pibble()
    print(pib.pibble())