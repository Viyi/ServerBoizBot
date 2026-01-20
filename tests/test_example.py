import pytest
import discord.ext.test as dpytest
import logging
from serverboizbot.main import load_extensions
from serverboizbot.bot.extensions.example import setup as setup_example

logger = logging.Logger(__name__)

# https://dpytest.readthedocs.io/en/latest/tutorials/using_pytest.html
# For non-python people the "bot" parameter is a pytest fixture
# It is defined in conftest.py

@pytest.mark.asyncio
async def test_bot_initialization(bot):
    """Make sure the bot can load extensions."""
    
    await load_extensions(bot)
    
    config = dpytest.get_config()
    username = config.members[0]
    
    await dpytest.message("!hello")
    
    assert dpytest.get_message().content == f"Hello {username}!"
    
@pytest.mark.asyncio
async def test_bot_hello(bot):
    """Here's an example test for just your extension."""
    await setup_example(bot)
    
    config = dpytest.get_config()
    username = config.members[0]
    
    await dpytest.message("!hello")
    
    assert dpytest.get_message().content == f"Hello {username}!"