import pypartpicker
import logging
import asyncio

logger = logging.getLogger(__name__)
logging.basicConfig(
level=logging.INFO, format="[%(levelname)s] %(name)s:%(lineno)s %(message)s"
)

async def get_ram_price() -> pypartpicker.Part:
    async with pypartpicker.AsyncClient() as pcpp:
        part = await pcpp.get_part("https://pcpartpicker.com/product/kTJp99/")

    return part

async def get_random_part():
    async with pypartpicker.AsyncClient() as pcpp:
        result = await pcpp.get_part_search("cpu", region="us")
        logger.critical(result)
        for part in result.parts:
            print(part)
    return result



if __name__ == "__main__":
    asyncio.run(get_random_part())


