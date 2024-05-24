class TicTacToeModel:
    def __init__(self, size_of_grid, size_of_win):
        self.size_of_grid = size_of_grid
        self.size_of_win = size_of_win
        self.board = [['' for _ in range(size_of_grid)] for _ in range(size_of_grid)]

    def setCurrentTurn(self, turn):
        self.current_turn = turn

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = 'X'


    def check_winner(self):

        def check_direction(start, direction, symbol):

            consecutive_count = 0

            dr, dc = direction
            # Check in the positive direction
            r, c = start

            while 0 <= r < self.size_of_grid and 0 <= c < self.size_of_grid:
                if self.board[r][c] == symbol:
                    consecutive_count += 1
                    if consecutive_count >= self.size_of_win:
                        return True

                else:
                    break

                r += dr
                c += dc

            # Check in the negative direction

            r, c = start[0] - dr, start[1] - dc

            while 0 <= r < self.size_of_grid and 0 <= c < self.size_of_grid:

                if self.board[r][c] == symbol:

                    consecutive_count += 1
                    if consecutive_count >= self.size_of_win:
                        return True

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
                if self.board[row][col] != '':
                    for direction in directions:
                        if check_direction((row, col), direction, self.board[row][col]):
                            return True

        return False

    def is_draw(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
