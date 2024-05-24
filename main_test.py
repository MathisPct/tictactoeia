# Test 2 profondeurs différentes
from algo.alpha_beta.alpha_beta import alpha_beta
from algo.alpha_beta.node_alpha_beta import NodeAlphaBeta
from algo.min_max.min_max import min_max
from algo.min_max.node_min_max import NodeMinMax
from model.tictactoemodel import TicTacToeModel

if __name__ == '__main__':
    size_of_grid = 5
    size_of_win = 4
    model = TicTacToeModel(size_of_grid, size_of_win)

    nb_win_1 = 0
    nb_win_2 = 0
    nb_draw = 0

    for i in range(10):
        finish = False
        print("Jeu :",str(i))
        while finish == False:

            root_player_1 = NodeAlphaBeta(model.board, 'O', model.size_of_win)
            model.board = alpha_beta(root_player_1, 2)

            print("------------------")
            for i in range(len(model.board)):
                print(model.board[i])

            if model.check_winner():
                finish = True
                print("1 Win")
                nb_win_1 += 1
                break

            if model.is_draw():
                finish = True
                print("Draw")
                nb_draw += 1
                break

            # fonction node min max
            root_player_2 = NodeAlphaBeta(model.board, 'X', model.size_of_win)
            model.board = alpha_beta(root_player_2, 2)
            print("------------------")
            for i in range(len(model.board)):
                print(model.board[i])

            if model.check_winner():
                finish = True
                print("2 Win")
                nb_win_2 += 1
                break

            if model.is_draw():
                finish = True
                print("Draw")
                break

    pourcentage_victoire_1 = nb_win_1 / 10 * 100
    pourcentage_victoire_2 = nb_win_2 / 10 * 100
    pourcentage_draw = nb_draw / 10 * 100

    print("Pourcentage victoire Joueur 1", pourcentage_victoire_1)
    print("Pourcentage victoire Joueur 2", pourcentage_victoire_2)
    print("Pourcentage égalité", pourcentage_draw)
