from typing import Union
from discord.ext import commands
from discord import Member, Reaction, User


class Heart(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: Reaction, user: Union[Member, User]):
        if reaction.emoji == "❤️" and user.id != self.bot.user.id:
            await reaction.message.add_reaction("❤️")
            await reaction.message.channel.send("❤️")


async def setup(bot: commands.Bot):
    await bot.add_cog(Heart(bot))
