from random import random
from time import time
import asyncio

async def rice():
    value = random() + 1
    print(f'Rice ready in {value} sec')
    await asyncio.sleep(value)
    print(f'Rice ready is finish.')
    return value

async def curry():
    value = random() + 1
    print(f'Curry ready in {value} sec')
    await asyncio.sleep(value)
    print(f'Curry ready is finish.')
    return value
async def noodle():
    value = random() + 1
    print(f'Noodle ready in {value} sec')
    await asyncio.sleep(value)
    print(f'Noodle ready is finish.')
    return value

async def main():
    start = time()
    tasks = [asyncio.create_task(rice(), name="rice"),asyncio.create_task(noodle(), name="noodle"),asyncio.create_task(curry(), name="curry") ]
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    first = done.pop()
    finish = time() - start
    print(first.get_name(), "is complete")
    print(first.get_name(),f'finish in {finish} sec')

asyncio.run(main())