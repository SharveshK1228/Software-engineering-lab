from game import SlidingPuzzle


def choose_size():
    while True:
        choice = input("Choose puzzle size (3, 4, or 5): ").strip()
        if choice in {"3", "4", "5"}:
            return int(choice)
        print("Please enter 3, 4, or 5.")


if __name__ == "__main__":
    SlidingPuzzle(choose_size()).run()
