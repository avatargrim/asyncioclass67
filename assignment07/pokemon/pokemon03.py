import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = 'asyncioclass67_6510301044/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'asyncioclass67_6510301044/assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    for path in pathlist:
        print(path)

asyncio.run(main())