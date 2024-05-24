from model.tictactoemodel import TicTacToeModel
from view.tictocview import TicTacToeView

if __name__ == '__main__':
    size_of_grid = 5  # Change this value to create a different size of the board
    size_of_win = 4
    model = TicTacToeModel(size_of_grid, size_of_win)
    view = TicTacToeView(model)

    view.run()

