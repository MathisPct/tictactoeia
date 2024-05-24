from algo.grid import Grid


class State:
    def __init__(self, grid: Grid, player, root_player):
        self.grid = grid
        self.player = player
        self.root_player = root_player

    def change_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def make_action(self, action):
        self.grid.make_action(action, self.player)

    def possible_actions(self):
        return self.grid.actions

    def is_terminal(self):
        return self.grid.is_full()

    def evalTotal(self):
        return self.eval(self.root_player) - self.eval("O" if self.root_player == "X" else "X")

    def eval(self, sign):
        total_score = 0
        nb_void = 0
        nb_used = 0

        # print("Signe :", sign)

        # test des valeurs de lignes
        for i in range(self.grid.size_of_grid):
            for j in range(self.grid.size_of_grid):
                if self.grid.symbol_at(i, j) == "":
                    nb_void += 1
                elif self.grid.symbol_at(i, j) == sign:
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                        # print("+ ", str(10 ** nb_used), " ligne ", str(i))
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
            if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                # print("+ ", str(10 ** nb_used), " ligne ", str(i))
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

        # test des valeurs de colones
        for i in range(self.grid.size_of_grid):
            for j in range(self.grid.size_of_grid):
                if self.grid.symbol_at(j, i) == "":
                    nb_void += 1
                elif (self.grid.symbol_at(j, i) == sign):
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.grid.size_of_grid and nb_used > 0:
                        # print("+ ", str(10 ** nb_used), " colonne ", str(i))
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
            if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                # print("+ ", str(10 ** nb_used), " colonne ", str(i))
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

        # test des valeurs de diagonales
        # diagonale principale

        init_col = 0
        init_row = self.grid.size_of_grid - self.grid.size_of_win

        while init_col <= self.grid.size_of_grid - self.grid.size_of_win:
            col = init_col
            row = init_row
            while col < self.grid.size_of_grid and row < self.grid.size_of_grid:
                if self.grid.symbol_at(row, col) == "":
                    nb_void += 1
                elif self.grid.symbol_at(row, col) == sign:
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                        # print("+ ", str(10 ** nb_used), " diag ", init_row, ":", init_col)
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
                col += 1
                row += 1

            if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                # print("+ ", str(10 ** nb_used), " diag ", init_row, ":", init_col)
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

            if (init_row == 0):
                init_col += 1
            else:
                init_row -= 1

        # diagonale principale secondaire
        init_col = 0
        init_row = self.grid.size_of_win - 1

        while init_col <= self.grid.size_of_grid - self.grid.size_of_win and init_row < self.grid.size_of_grid:
            col = init_col
            row = init_row
            while col < self.grid.size_of_grid and row >= 0:
                if self.grid.symbol_at(row, col) == "":
                    nb_void += 1
                elif self.grid.symbol_at(row, col) == sign:
                    nb_used += 1
                else:
                    if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                        # print("+ ", str(10 ** nb_used), " anti diag ", init_row, ":", init_col)
                        total_score += 10 ** nb_used
                    nb_used = 0
                    nb_void = 0
                col += 1
                row -= 1

            if nb_used + nb_void >= self.grid.size_of_win and nb_used > 0:
                # print("+ ", str(10 ** nb_used), " anti diag ", init_row, ":", init_col)
                total_score += 10 ** nb_used
            nb_used = 0
            nb_void = 0

            if (init_row == self.grid.size_of_grid - 1):
                init_col += 1
            else:
                init_row += 1

        return total_score

    def copy(self):
        return State(self.grid, self.player, self.root_player)