import pypartpicker
import logging

logger = logging.getLogger(__name__)

async def get_ram_price() -> pypartpicker.Part:
    async with pypartpicker.AsyncClient() as pcpp:
        part = await pcpp.get_part("https://pcpartpicker.com/product/kTJp99/")

    return part


