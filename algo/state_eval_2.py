from algo.state import State


class StateEval2(State):
    def __init__(self, grid, player, root_player):
        super().__init__(grid, player, root_player)

    def eval(self, sign):
        return self.eval_2(sign)

    def copy(self):
        return StateEval2(self.grid.copy(), self.player, self.root_player)