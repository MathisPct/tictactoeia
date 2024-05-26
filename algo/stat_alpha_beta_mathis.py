import random

from algo.alpha_beta_test_mathis import alpha_beta
from algo.grid import Grid
from algo.mini_max_mathis import min_max
from algo.state import State
from algo.state_eval_2 import StateEval2
from algo.state_eval_immediate import StateEvalImmediate

if __name__ == '__main__':
    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    trying = 1
    for i in range(trying):
        size_of_grid = 6
        size_of_win = 4
        grid = Grid(size_of_grid, size_of_win)
        while grid.is_full() is False and grid.check_winner() is None:
            root_player_1 = StateEvalImmediate(grid.copy(), player_1, player_1)
            action_player_1 = min_max(root_player_1, 3)
            grid.make_action(action_player_1, player_1)
            print("Le joueur 1 a joué :")
            print(grid)

            if grid.is_full() or grid.check_winner() is not None:
                break

            root_player_2 = StateEvalImmediate(grid.copy(), player_2, player_2)
            action_player_2 = alpha_beta(root_player_2, 3)
            grid.make_action(action_player_2, player_2)
            # fonction aléatoire
            # grid.make_action(random.choice(grid.actions), player_2)

            print("Le joueur 2 a joué :")
            print(grid)
        print("Fin de la partie")

        win_player = grid.check_winner()
        if win_player == player_1:
            nb_win_1 += 1
        elif win_player == player_2:
            nb_win_2 += 1
        else:
            nb_draw += 1

    pourcentage_victoire_1 = (nb_win_1 / trying) * 100
    pourcentage_victoire_2 = (nb_win_2 / trying) * 100
    pourcentage_draw = (nb_draw / trying) * 100

    print("Pourcentage victoire Joueur 1", pourcentage_victoire_1)
    print("Pourcentage victoire Joueur 2", pourcentage_victoire_2)
    print("Pourcentage égalité", pourcentage_draw)
