import random
import time

from algo.alpha_beta import alpha_beta
from model.grid import Grid
from algo.mini_max import min_max
from algo.state_eval_2 import StateEval2
from algo.state_eval_immediate import StateEvalImmediate


def alpha_beta_vs_mini_max_execution_time(size_of_grid=6, size_of_win=4):
    player_1 = 'O'
    player_2 = 'X'

    grid = Grid(size_of_grid, size_of_win)
    while grid.is_full() is False and grid.check_winner() is None:
        root_player_2 = StateEvalImmediate(grid.copy(), player_2, player_2)
        start_alpha_beta = time.time()
        action_player_2 = alpha_beta(root_player_2, 3)
        end_alpha_beta = time.time()
        print("Temps alpha beta : ", end_alpha_beta - start_alpha_beta)
        grid.make_action(action_player_2, player_2)

        print("Le joueur 2 a joué :")
        print(grid)

        if grid.is_full() or grid.check_winner() is not None:
            break

        root_player_1 = StateEvalImmediate(grid.copy(), player_1, player_1)
        start_min_max = time.time()
        action_player_1 = min_max(root_player_1, 3)
        end_min_max = time.time()
        print("Temps minimax : ", end_min_max - start_min_max)
        grid.make_action(action_player_1, player_1)
        print("Le joueur 1 a joué :")
        print(grid)

    print("Fin de la partie")

def alpha_beta_vs_mini_max_win_rate(size_of_grid=6, size_of_win=4, trying=10):
    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(trying):
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

def win_rate_alpha_beta_depth_difference(depth_1, depth_2, size_of_grid=6, size_of_win=4, trying=10):
    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(trying):
        grid = Grid(size_of_grid, size_of_win)
        while grid.is_full() is False and grid.check_winner() is None:
            root_player_1 = StateEvalImmediate(grid.copy(), player_1, player_1)
            action_player_1 = alpha_beta(root_player_1, depth_1)
            grid.make_action(action_player_1, player_1)
            print("Le joueur 1 a joué :")
            print(grid)

            if grid.is_full() or grid.check_winner() is not None:
                break

            root_player_2 = StateEvalImmediate(grid.copy(), player_2, player_2)
            action_player_2 = alpha_beta(root_player_2, depth_2)
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

def win_rate_alpha_beta_vs_random(depth_1, size_of_grid=6, size_of_win=4, trying=100):
    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(trying):
        grid = Grid(size_of_grid, size_of_win)
        while grid.is_full() is False and grid.check_winner() is None:
            root_player_1 = StateEvalImmediate(grid.copy(), player_1, player_1)
            action_player_1 = alpha_beta(root_player_1, depth_1)
            grid.make_action(action_player_1, player_1)
            print("Le joueur 1 a joué :")
            print(grid)

            if grid.is_full() or grid.check_winner() is not None:
                break

            # fonction aléatoire
            grid.make_action(random.choice(grid.actions), player_2)

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

def win_rate_alpha_beta_eval2_vs_random(depth_1, size_of_grid=6, size_of_win=4, trying=100):
    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(trying):
        grid = Grid(size_of_grid, size_of_win)
        while grid.is_full() is False and grid.check_winner() is None:
            root_player_1 = StateEval2(grid.copy(), player_1, player_1)
            action_player_1 = alpha_beta(root_player_1, depth_1)
            grid.make_action(action_player_1, player_1)
            print("Le joueur 1 a joué :")
            print(grid)

            if grid.is_full() or grid.check_winner() is not None:
                break

            # fonction aléatoire
            grid.make_action(random.choice(grid.actions), player_2)

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


def win_rate_alpha_beta_eval2_vs_eval3(depth_1, depth_2, size_of_grid=6, size_of_win=4, trying=10):
    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(trying):
        grid = Grid(size_of_grid, size_of_win)
        while grid.is_full() is False and grid.check_winner() is None:
            root_player_1 = StateEval2(grid.copy(), player_1, player_1) # Eval 2
            action_player_1 = alpha_beta(root_player_1, depth_1)
            grid.make_action(action_player_1, player_1)
            print("Le joueur 1 a joué :")
            print(grid)

            if grid.is_full() or grid.check_winner() is not None:
                break

            # fonction aléatoire
            root_player_2 = StateEvalImmediate(grid.copy(), player_2, player_2) # Eval 3
            action_player_2 = alpha_beta(root_player_2, depth_2)
            grid.make_action(action_player_2, player_2)

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


if __name__ == '__main__':
    alpha_beta_vs_mini_max_execution_time()
