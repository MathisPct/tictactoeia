from model.tictactoemodel import TicTacToeModel
from view.tictocview import TicTacToeView

if __name__ == '__main__':
    size_of_grid = 6
    size_of_win = 4
    view = TicTacToeView(size_of_grid, size_of_win)

    view.run()

