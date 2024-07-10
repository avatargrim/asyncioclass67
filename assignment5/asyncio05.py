from random import random
import asyncio

async def rice():
    value = random() + 1
    await asyncio.sleep(value)
    return f'Rice ready in {value} sec'

async def curry():
    value = random() + 1
    await asyncio.sleep(value)
    return f'Curry ready in {value} sec'
 
async def noodle():
    value = random() + 1
    await asyncio.sleep(value)
    return f'Noodle ready in {value} sec'


async def main():
    tasks = [asyncio.create_task(rice()),asyncio.create_task(noodle()),asyncio.create_task(curry()) ]
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for task in done:
        print(task.result())


asyncio.run(main())