import time
import asyncio

class chess_game:
    pass

class chess_move:
    pass


async def chess(num):
    print(f"Begin game",num+1)
    for game in range(moves):
        print("judit", game+1)
        time.sleep(judit)
        print("opponent", game+1)
        await asyncio.sleep(opponent)
    return chess_game()

async def main():
    coros = [chess(i) for i in range(total_opponent)]

    await asyncio.gather(*coros)


if __name__ == "__main__":
    start_game = time.perf_counter()
    judit = 0.1
    opponent = 0.5
    moves = 30
    total_opponent = 24
    
    asyncio.run(main())

    elapsed = time.perf_counter() - start_game
    print(f"All chess game play {round(elapsed)} second")