import pytest
import discord.ext.test as dpytest
import logging
from serverboizbot.main import load_extensions

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_git_info(bot):
    """Try the git info command to get simple information."""

    await load_extensions(bot)

    await dpytest.message("!git info")

    assert "Git Repository Stats" in dpytest.get_message().content
