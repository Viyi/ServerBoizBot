from discord.ext import commands
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
            logger.info("Fortnite? Are you SERIOUS?")
            await message.channel.send("This incident will be reported.")

    # Commands are invoked by members.
    # using a commands.hybrid_command means it'll work with the ! or /
    # note: the / commands are slow to sync, there is a !sync command defined in main
    @commands.hybrid_command(name="hello", description="Says hello!")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author}!")


# main.py will look for this setup command to initialize your code
async def setup(bot: commands.Bot):
    await bot.add_cog(Example(bot))
