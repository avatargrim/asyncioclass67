import aiofiles
import asyncio
import json

pokemonapi_directory='/assingment7/pokemon/pokemonapi'
pokemonmove_directory='/assingment7/pokemon/pokemonmove'

async def main():
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json',mode='r') as f:
        contents= await f.read()

    pokemon=json.loads(contents)
    print(pokemon['name'])


asyncio.run(main())