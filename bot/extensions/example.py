from discord.ext import commands
from discord import app_commands
import discord
import logging

logger = logging.getLogger(__name__)


# Here is an example discord.py extension/cog
class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Listeners can be used to react to events
    @commands.Cog.listener()
    async def on_message(self, message):
        if "fortnite" in message.content:
            logger.info("Fortnite detected!")
            await message.channel.send("Ban Him!")

    # Commands are invoked by members.
    # using a commands.hybrid_command means it'll work with the ! or /
    # note: the / commands are slow to sync, there is a !sync command defined in main, that SHOULD force sync them.
    @commands.hybrid_command(name="hello", description="Says hello to a member")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author}!")


# main.py will look for this setup command to initialize your code
async def setup(bot: commands.Bot):
    await bot.add_cog(Example(bot))
