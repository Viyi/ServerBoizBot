import discord
import discord.ext.commands as commands
import pytest_asyncio
import discord.ext.test as dpytest
from serverboizbot.main import setup_bot

@pytest_asyncio.fixture
async def bot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!",
                     intents=intents)
    
    bot = setup_bot(bot)

    await bot._async_setup_hook()  
    
    dpytest.configure(bot)

    yield bot

    await dpytest.empty_queue() 