import asyncio
from time import sleep,time

async def make_coffee():
    print("coffee: prepare ingriditends")
    sleep(1)
    print("coffee:waiting...")
    await asyncio.sleep(5)
    print("coffee:ready")

async def fry_eggs():
    print("eggs prepare ingriditends")
    sleep(1)
    print("egg frying...")
    await asyncio.sleep(3)
    print("eggs:ready")

async def main():
    start=time()
    await make_coffee()
    await fry_eggs()
    print(f"breakfast is ready in {time()-start} min")

asyncio.run(main())