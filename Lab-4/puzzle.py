import random


class Puzzle:
    """Sliding-puzzle board and movement rules."""

    DIRECTIONS = {
        "w": (-1, 0),
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1),
    }

    def __init__(self, size=4):
        if size not in (3, 4, 5):
            raise ValueError("Puzzle size must be 3, 4, or 5.")
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        """Create an unsolved board that is guaranteed to be reachable.

        Start from the solved arrangement and scramble it only with legal
        blank-space moves. Every generated position is therefore solvable.
        """
        board = self._solved_board()
        blank_r = self.size - 1
        blank_c = self.size - 1
        previous_blank = None

        # Enough legal moves to give a useful scramble at every supported size.
        scramble_steps = self.size * self.size * 20

        for _ in range(scramble_steps):
            neighbours = []
            for dr, dc in self.DIRECTIONS.values():
                nr, nc = blank_r + dr, blank_c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    neighbours.append((nr, nc))

            # Avoid immediately undoing the previous scramble move when possible.
            choices = [pos for pos in neighbours if pos != previous_blank]
            if not choices:
                choices = neighbours

            nr, nc = random.choice(choices)
            board[blank_r][blank_c], board[nr][nc] = (
                board[nr][nc],
                board[blank_r][blank_c],
            )
            previous_blank = (blank_r, blank_c)
            blank_r, blank_c = nr, nc

        # Extremely rarely a long scramble can return to the solved position.
        # If it does, make one additional legal move so gameplay never starts done.
        if self._is_solved_board(board):
            for dr, dc in self.DIRECTIONS.values():
                nr, nc = blank_r + dr, blank_c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    board[blank_r][blank_c], board[nr][nc] = (
                        board[nr][nc],
                        board[blank_r][blank_c],
                    )
                    break

        return board

    def _solved_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]
        return [
            tiles[r * self.size : (r + 1) * self.size]
            for r in range(self.size)
        ]

    def _is_solved_board(self, board):
        expected = list(range(1, self.size * self.size)) + [0]
        return [value for row in board for value in row] == expected

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c
        raise ValueError("Puzzle board has no blank tile.")

    def move(self, direction):
        """Move the blank in the requested direction.

        Returns True only when a tile actually slides. Once the puzzle is solved,
        movement is locked so completed games cannot be changed.
        """
        if direction not in self.DIRECTIONS or self.solved():
            return False

        r, c = self.blank_pos()
        dr, dc = self.DIRECTIONS[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
        return True

    def solved(self):
        return self._is_solved_board(self.board)
