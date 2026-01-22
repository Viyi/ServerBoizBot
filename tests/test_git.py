import pytest
import discord.ext.test as dpytest
import logging
from serverboizbot.main import load_extensions
from serverboizbot.bot.extensions.example import setup as setup_example

logger = logging.getLogger(__name__)



@pytest.mark.asyncio
async def test_git_info(bot):
    """Try the git info command to get simple information."""
    
    await load_extensions(bot)
    
    config = dpytest.get_config()
    username = config.members[0]
    
    await dpytest.message("!git info")
    
    assert "Git Info" in dpytest.get_message().content 
    
