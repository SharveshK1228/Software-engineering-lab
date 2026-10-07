import time

from puzzle import Puzzle


class SlidingPuzzle:
    """Interactive game session with timer and move tracking."""

    def __init__(self, size=4):
        if size not in (3, 4, 5):
            raise ValueError("Puzzle size must be 3, 4, or 5.")

        self.size = size
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.finished_at = None
        self.completed = False

    def elapsed_seconds(self):
        end = self.finished_at if self.finished_at is not None else time.monotonic()
        return int(end - self.started)

    def display(self):
        print()
        width = len(str(self.size * self.size - 1))
        for row in self.puzzle.board:
            print(" ".join(f"{value or ' ':>{width}}" for value in row))
        print(f"Size: {self.size}x{self.size}  Moves: {self.moves}  Time: {self.elapsed_seconds()}s")

    def attempt_move(self, key):
        """Apply one gameplay move and update session state consistently."""
        if self.completed:
            return False

        moved = self.puzzle.move(key)
        if not moved:
            return False

        self.moves += 1
        if self.puzzle.solved():
            self.completed = True
            self.finished_at = time.monotonic()
        return True

    def run(self):
        print("Sliding Puzzle — W/A/S/D moves the blank. Q quits.")

        while not self.completed:
            self.display()
            key = input("> ").strip().lower()

            if key == "q":
                print("Game ended.")
                return

            if key not in {"w", "a", "s", "d"}:
                print("Invalid command. Use W/A/S/D or Q.")
                continue

            if self.attempt_move(key):
                print("Moved.")
            else:
                print("That move is not possible.")

        self.display()
        print(f"Solved in {self.moves} moves and {self.elapsed_seconds()} seconds!")
