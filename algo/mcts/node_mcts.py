class NodeMcts:
    def __init__(self, board, current_turn, size_of_win, parent=None):
        self.board = board
        self.current_turn = current_turn
        self.size_of_win = size_of_win
        self.children = []
        self.score = 0
        self.nb_passage = 0
        self.parent = parent
        self.untried_moves = [(i, j) for i in range(len(self.board)) for j in range(len(board[i])) if board[i][j] == '']

    def is_winning(self, x, y) -> bool:
        sign = self.board[x][y]
        size = len(self.board)

        # Check row
        count = 0
        for i in range(size):
            if self.board[x][i] == sign:
                count += 1
                if count >= self.size_of_win:
                    return True
            else:
                count = 0

        # Check column
        count = 0
        for i in range(size):
            if self.board[i][y] == sign:
                count += 1
                if count >= self.size_of_win:
                    return True
            else:
                count = 0

        # Check diagonal (top-left to bottom-right)
        count = 0
        for i in range(-self.size_of_win + 1, self.size_of_win):
            new_x, new_y = x + i, y + i
            if 0 <= new_x < size and 0 <= new_y < size:
                if self.board[new_x][new_y] == sign:
                    count += 1
                    if count >= self.size_of_win:
                        return True
                else:
                    count = 0

        # Check diagonal (top-right to bottom-left)
        count = 0
        for i in range(-self.size_of_win + 1, self.size_of_win):
            new_x, new_y = x + i, y - i
            if 0 <= new_x < size and 0 <= new_y < size:
                if self.board[new_x][new_y] == sign:
                    count += 1
                    if count >= self.size_of_win:
                        return True
                else:
                    count = 0

        return False

    def is_non_terminal(self):
        for row in self.board:
            if '' in row:
                return True
        return False

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0

    def generate_children(self):
        next_turn = 'O' if self.current_turn == 'X' else 'X'
        while self.untried_moves:
            i, j = self.untried_moves.pop()
            new_board = [row[:] for row in self.board]
            new_board[i][j] = self.current_turn
            self.children.append(NodeMcts(new_board, next_turn, self.size_of_win, self))
