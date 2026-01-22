from discord.ext import commands
from serverboizbot.core.git_repo import git_info
import logging

logger = logging.getLogger(__name__)


class Git(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_group(name="git", description="Git repository commands")
    async def git_group(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please specify a subcommand: `info`, etc.")

    @git_group.command(name="info", description="returns current git info!")
    async def info(self, ctx):
        await ctx.send(git_info())


async def setup(bot: commands.Bot):
    await bot.add_cog(Git(bot))
