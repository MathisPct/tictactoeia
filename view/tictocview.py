import pygame
import sys

from algo.alpha_beta import alpha_beta
from model.grid import Grid
from algo.state_eval_2 import StateEval2
from algo.state_eval_immediate import StateEvalImmediate


class TicTacToeView:
    def __init__(self, grid_size, size_of_win):
        self.grid = Grid(grid_size, size_of_win)

        self.size = 600
        self.cell_size = self.size // self.grid.size_of_grid
        pygame.init()
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption('Tic Tac Toe')
        self.font = pygame.font.Font(None, 60)
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        self.screen.fill((255, 255, 255))
        for row in range(self.grid.size_of_grid):
            for col in range(self.grid.size_of_grid):
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
                if self.grid.grid[row][col] != '':
                    text = self.font.render(self.grid.grid[row][col], True, (0, 0, 0))
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

    def check_is_winner_or_draw(self):
        winner = self.grid.check_winner()
        if winner is not None:
            text = self.font.render('wins!', True, (255, 0, 0))
            self.screen.blit(text, (self.size // 2 - text.get_width() // 2, self.size // 2 - text.get_height() // 2))
        elif self.grid.is_full():
            text = self.font.render('Draw!', True, (255, 0, 0))
            self.screen.blit(text, (self.size // 2 - text.get_width() // 2, self.size // 2 - text.get_height() // 2))

    def handle_click(self, pos):
        if self.grid.check_winner() is not None or self.grid.is_full():
            return

        row, col = pos[1] // self.cell_size, pos[0] // self.cell_size
        self.grid.make_action((row, col), 'O')

        if self.grid.check_winner() is not None or self.grid.is_full():
            return

        root_player_2 = StateEval2(self.grid, 'X', 'X')
        root_player_2 = StateEvalImmediate(self.grid, 'X', 'X')
        action_player_2 = alpha_beta(root_player_2, 3)
        self.grid.make_action(action_player_2, 'X')
        # root_player_2 = NodeMcts(self.grid.grid, 'X', self.grid.size_of_win)
        # self.grid.grid = uct_search(root_player_2, 'X', self.grid.size_of_win).board

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())

            self.draw_grid()
            self.check_is_winner_or_draw()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()
