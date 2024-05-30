class Grid:
    def __init__(self, grid_size, size_of_win, grid=None):
        self.size_of_grid = grid_size
        self.size_of_win = size_of_win
        self.grid = grid or [["" for _ in range(grid_size)] for _ in range(grid_size)]
        self.actions = [(i, j) for i in range(grid_size) for j in range(grid_size) if self.grid[i][j] == ""]

    def __str__(self):
        return '\n'.join([' '.join([str(cell) if cell!= "" else "." for cell in row]) for row in self.grid])

    def symbol_at(self, row, col):
        return self.grid[row][col]

    def make_action(self, action, player):
        if action in self.actions:
            self.grid[action[0]][action[1]] = player
            self.actions.remove(action)
        else:
            print(f"Action {action} not found in the list of actions.")

    def is_full(self):
        return len(self.actions) == 0

    """
    Check if there is a winner
    :return: the symbol of the winner or None if there is no winner
    """
    def check_winner(self):

        def check_direction(start, direction, symbol):

            consecutive_count = 0

            dr, dc = direction
            # Check in the positive direction
            r, c = start

            while 0 <= r < self.size_of_grid and 0 <= c < self.size_of_grid:
                if self.grid[r][c] == symbol:
                    consecutive_count += 1
                    if consecutive_count >= self.size_of_win:
                        return symbol

                else:
                    break

                r += dr
                c += dc

            # Check in the negative direction

            r, c = start[0] - dr, start[1] - dc

            while 0 <= r < self.size_of_grid and 0 <= c < self.size_of_grid:

                if self.grid[r][c] == symbol:

                    consecutive_count += 1
                    if consecutive_count >= self.size_of_win:
                        return symbol

                else:
                    break

                r -= dr

                c -= dc

            return False

        directions = [
            (1, 0),  # Vertical
            (0, 1),  # Horizontal
            (1, 1),  # Main diagonal
            (1, -1)  # Anti diagonal

        ]

        for row in range(self.size_of_grid):
            for col in range(self.size_of_grid):
                if self.grid[row][col] != '':
                    for direction in directions:
                        if check_direction((row, col), direction, self.grid[row][col]):
                            return self.grid[row][col]

        return None

    def copy(self):
        return Grid(self.size_of_grid, self.size_of_win, grid=[row.copy() for row in self.grid])