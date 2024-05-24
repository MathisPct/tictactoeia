import math


class NodeAlphaBeta2:
    def __init__(self, board, current_turn, win_size):
        self.board = board
        self.current_turn = current_turn
        self.win_size=win_size

    def is_leaf(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == "":
                    return False
        return True

    def evalTotal(self):
        if self.current_turn == "X":
            return self.eval("X") - self.eval("O")
        else:
            return self.eval("O") - self.eval("X")

    def eval(self, sign):
        total_score = 0
        nb_void = 0
        nb_used = 0

        #print("Signe :", sign)

        # test des valeurs de lignes
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == "":
                    nb_void += 1
                elif (self.board[i][j] == sign):
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                        #print("+ ", str(10 ** nb_used), " ligne ", str(i))
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
            if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                #print("+ ", str(10 ** nb_used), " ligne ", str(i))
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

        # test des valeurs de colones
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[j][i] == "":
                    nb_void += 1
                elif (self.board[j][i] == sign):
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                        #print("+ ", str(10 ** nb_used), " colonne ", str(i))
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
            if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                #print("+ ", str(10 ** nb_used), " colonne ", str(i))
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

        # test des valeurs de diagonales
        # diagonale principale

        init_col = 0
        init_row = len(self.board) - self.size_of_win

        while (init_col <= len(self.board) - self.size_of_win):
            col = init_col
            row = init_row
            while (col < len(self.board) and row < len(self.board)):
                if self.board[row][col] == "":
                    nb_void += 1
                elif (self.board[row][col] == sign):
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                        #print("+ ", str(10 ** nb_used), " diag ", init_row, ":", init_col)
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
                col += 1
                row += 1

            if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                #print("+ ", str(10 ** nb_used), " diag ", init_row, ":", init_col)
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

            if (init_row == 0):
                init_col += 1
            else:
                init_row -= 1

        # diagonale principale secondaire
        init_col = 0
        init_row = self.size_of_win - 1

        while init_col <= len(self.board) - self.size_of_win and init_row < len(self.board):
            col = init_col
            row = init_row
            while (col < len(self.board) and row >= 0):
                if self.board[row][col] == "":
                    nb_void += 1
                elif (self.board[row][col] == sign):
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                        #print("+ ", str(10 ** nb_used), " anti diag ", init_row, ":", init_col)
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
                col += 1
                row -= 1

            if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                #print("+ ", str(10 ** nb_used), " anti diag ", init_row, ":", init_col)
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

            if (init_row == len(self.board) - 1):
                init_col += 1
            else:
                init_row += 1

        return total_score

def alpha_beta(root_player, depth):
    max_value, action = player_max(root_player, depth, -math.inf,math.inf)


def player_max(node, depth, alpha, beta):
    if depth==0 or node.is_leaf():
        return total_ev(n), None

