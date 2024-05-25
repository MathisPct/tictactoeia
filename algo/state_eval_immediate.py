from algo.state import State


class StateEvalImmediate(State):
    def __init__(self, grid, player, root_player):
        super().__init__(grid, player, root_player)

    def eval(self, sign):
        return self.eval_3(sign)

    def copy(self):
        return StateEvalImmediate(self.grid.copy(), self.player, self.root_player)