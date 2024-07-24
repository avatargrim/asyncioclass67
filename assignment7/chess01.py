import time

class chess_game:
    pass

class chess_move:
    pass

def move(play):
    for i in range(play):
        print("opponent move chess")
        time.sleep(0.05)
        print("Judit move chess")
        time.sleep(0.01)
    return chess_move    

def chess(num):
    for game in range(num):
        start_game = time.perf_counter()
        print(f"{time.ctime()} - Begin game",game+1)
        move(30)
        print(f"{time.ctime()} - End game",game+1)
        elapsed = time.perf_counter() - start_game
        print(f"{time.ctime()} chess game play ", elapsed*1000, "second.")
    return chess_game()

def main():
    chess(24)

if __name__ == "__main__":
    start_game = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_game
    print(f"{time.ctime()} All chess game play ", (elapsed*1000)/60, "minutes.")
