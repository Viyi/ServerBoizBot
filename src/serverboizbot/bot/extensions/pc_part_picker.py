from discord.ext import commands
from serverboizbot.core.pc_part_picker import get_ram_price
import logging

logger = logging.getLogger(__name__)


# Here is an example discord.py extension/cog
class PcPartPicker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

  
    @commands.hybrid_command(name="ram", description="Check ram price!")
    async def hello(self, ctx):
        
        msg = await ctx.send("Checking ram cost... ")
        ram = get_ram_price()
        
        await msg.edit(content=f"Found it!\n{ram.name} costs {ram.cheapest_price} at only {ram.spec['Price / GB']} / GB\nWhat a deal!")
        
        


# main.py will look for this setup command to initialize your code
async def setup(bot: commands.Bot):
    await bot.add_cog(PcPartPicker(bot))
