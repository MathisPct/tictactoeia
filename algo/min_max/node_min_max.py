class NodeMinMax:
    def __init__(self, board, current_turn, size_of_win):
        self.board = board
        self.current_turn = current_turn
        self.size_of_win = size_of_win
        self.children_node = []

    def evalTotal(self, root_player_sign):
        #for i in range(len(self.board)):
            #print(self.board[i])
        # if self.current_turn == "X":
        #     #print("calc X")
        #     x=self.eval("X")
        #     #print("calc O")
        #     o=self.eval("O")
        #     #print("X - O = ",str(x-o))
        #     return x-o
        #     #return self.eval("X") - self.eval("O")
        # else:
        #     #print("calc O")
        #     o = self.eval("O")
        #     #print("calc X")
        #     x = self.eval("X")
        #     #print("O - X = ", str(o-x))
        #     return o-x

        #print(root_player.current_turn)
        arg_1=self.eval(root_player_sign)

        #print("X" if root_player.current_turn == "O" else "O")
        arg_2=self.eval("X" if root_player_sign == "O" else "O")

        res=arg_1-arg_2

        #print(root_player_sign," - ","X" if root_player_sign == "O" else "O"," = ",str(res))
        return res

    def eval(self, sign):
        total_score = 0
        nb_void = 0
        nb_used = 0

        ##print("Signe :", sign)

        # test des valeurs de lignes
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == "":
                    nb_void += 1
                elif (self.board[i][j] == sign):
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                        total_score += 10 ** nb_used
                        #print("+ ",str(10 ** nb_used)," ligne ",str(i))
                    nb_used = 0
                    nb_void = 0
            if nb_used + nb_void >= self.size_of_win and nb_used > 0:
                total_score += 10 ** nb_used
                #print("+ ", str(10 ** nb_used), " ligne ", str(i))
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
        # diagonale #principale

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

        # diagonale #principale secondaire
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

    def is_leaf(self):
        return len(self.children_node) == 0

    def is_not_leaf(self):
        return not self.is_leaf()

    def generate_children(self):
        next_turn = 'O' if self.current_turn == 'X' else 'X'
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '':
                    new_board = [r.copy() for r in self.board]
                    new_board[row][col] = next_turn
                    self.children_node.append(NodeMinMax(new_board, next_turn, self.size_of_win))
