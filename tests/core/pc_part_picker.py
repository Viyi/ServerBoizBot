import pytest
from serverboizbot.core.pc_part_picker import get_ram_price

import logging

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_ram_price():
    ram = await get_ram_price()
            
    logger.info(f"Found it!\n{ram.name} costs {ram.cheapest_price}\nThat is {ram.specs['Price / GB']} / GB!\nWhat a deal!")