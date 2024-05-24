import math


class NodeMcts:
    def __init__(self, board, current_turn, size_of_win, parent=None):
        self.board = board
        self.current_turn = current_turn
        self.size_of_win = size_of_win
        self.children = []
        self.score = 0
        self.nb_passage = 0
        self.parent = parent

    def is_winning(self, x, y):
        sign = self.board[x][y]
        nb_sign = 0

        # test des valeurs de lignes
        for i in range(max(0, x - self.size_of_win + 1), min(len(self.board), x + self.size_of_win - 1)):
            if self.board[i][y] == sign:
                nb_sign += 1
                if nb_sign >= self.size_of_win:
                    return True
            else:
                nb_sign = 0

        # test des valeurs de colones
        for i in range(max(0, y - self.size_of_win + 1), min(len(self.board), y + self.size_of_win - 1)):
            if self.board[x][i] == sign:
                nb_sign += 1
                if nb_sign >= self.size_of_win:
                    return True
            else:
                nb_sign = 0

        # test des valeurs de diagonales
        # diagonale principale

        for i in range(max(0, x - self.size_of_win + 1), min(len(self.board), x + self.size_of_win - 1)):
            if (0 <= y + (i - x) < len(self.board)):
                if self.board[i][y + (i - x)] == sign:
                    nb_sign += 1
                    if nb_sign >= self.size_of_win:
                        return True
                else:
                    nb_sign = 0

        for i in range(max(0, x - self.size_of_win + 1), min(len(self.board), x + self.size_of_win - 1)):
            if (0 <= y - (i - x) < len(self.board)):
                if self.board[i][y - (i - x)] == sign:
                    nb_sign += 1
                    if nb_sign >= self.size_of_win:
                        return True
                else:
                    nb_sign = 0

        return False

    def is_non_terminal(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == '':
                    return True
        return False

    def is_fully_expanded(self):
        nb_possible_children = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == '':
                    nb_possible_children += 1
        return nb_possible_children == len(self.children)

    def is_leaf(self):
        return len(self.children) == 0

    def is_not_leaf(self):
        return not self.is_leaf()

    def generate_children(self):
        next_turn = 'O' if self.current_turn == 'X' else 'X'
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '':
                    new_board = [r.copy() for r in self.board]
                    new_board[row][col] = next_turn
                    self.children.append(NodeMcts(new_board, next_turn, self.size_of_win))
