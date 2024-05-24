from algo.alpha_beta_test_mathis import alpha_beta
from algo.grid import Grid
from algo.state import State

if __name__ == '__main__':
    size_of_grid = 3
    size_of_win = 3
    grid = Grid(size_of_grid, size_of_win)

    player_1 = 'O'
    player_2 = 'X'

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(10):
        while grid.is_full() is False and grid.check_winner() is None:
            root_player_1 = State(grid, player_1, player_1)
            action_player_1 = alpha_beta(root_player_1, 1)
            grid.make_action(action_player_1, player_1)
            print("Le joueur 1 a joué :")
            print(grid)

            # fonction node min max
            root_player_2 = State(grid, player_2, player_2)
            action_player_2 = alpha_beta(root_player_2, 3)
            grid.make_action(action_player_2, player_2)
            print("Le joueur 2 a joué :")
            print(grid)
        print("Fin de la partie")

        win_player = grid.check_winner()
        if win_player == player_1:
            nb_win_1 += 1
        elif win_player == player_2:
            nb_win_2 += 2
        else:
            nb_draw += 1


    pourcentage_victoire_1 = nb_win_1 / 10 * 100
    pourcentage_victoire_2 = nb_win_2 / 10 * 100
    pourcentage_draw = nb_draw / 10 * 100

    print("Pourcentage victoire Joueur 1", pourcentage_victoire_1)
    print("Pourcentage victoire Joueur 2", pourcentage_victoire_2)
    print("Pourcentage égalité", pourcentage_draw)
