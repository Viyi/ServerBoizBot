import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
from pathlib import Path


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] %(name)s:%(lineno)s %(message)s"
)

logger = logging.getLogger(__name__)

if not os.getenv("DISCORD_TOKEN"):
    logger.critical("DISCORD_TOKEN token expected in .env!")


async def load_extensions(bot):
    for filename in os.listdir(BASE_DIR / "bot/extensions"):
        if filename.endswith(".py") and not filename.startswith("__"):
            await bot.load_extension(f"serverboizbot.bot.extensions.{filename[:-3]}")


async def check_sync_required(bot: commands.Bot):
    remote_commands = await bot.tree.fetch_commands()
    local_commands = bot.tree.get_commands()

    return len(remote_commands) != len(local_commands)


def setup_bot(bot: commands.Bot):
    
    @bot.command()
    async def sync(ctx):
        # Use this command to quickly sync /commands with !sync
        bot.tree.copy_global_to(guild=ctx.guild)
        synced = await bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(synced)} commands to this guild.")

    @bot.event
    async def on_ready():
        logger.info(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

        if await check_sync_required(bot):
            try:
                synced = await bot.tree.sync()
                logger.info(f"Synced {len(synced)} command(s)")
            except Exception as e:
                logger.error(f"Failed to sync commands: {e}")

        logger.info("Bot is initialized, have fun!")
        
    return bot

async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)
    
    bot = setup_bot(bot)
    
    async with bot:
        await load_extensions(bot)
        await bot.start(os.getenv("DISCORD_TOKEN"))


def start():
    asyncio.run(main())
    

if __name__ == "__main__":
    logger.info("Starting Bot")
    asyncio.run(main())
