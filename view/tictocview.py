import pygame
import sys

from algo.alpha_beta.alpha_beta import alpha_beta
from algo.alpha_beta.node_alpha_beta import NodeAlphaBeta
from algo.min_max.min_max import min_max
from algo.min_max.node_min_max import NodeMinMax
from algo.mcts.node_mcts import NodeMcts
from algo.mcts.mcts import *



class TicTacToeView:
    def __init__(self, model):
        self.model = model

        self.size = 600
        self.cell_size = self.size // self.model.size_of_grid
        pygame.init()
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption('Tic Tac Toe')
        self.font = pygame.font.Font(None, 60)
        self.clock = pygame.time.Clock()

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for row in range(self.model.size_of_grid):
            for col in range(self.model.size_of_grid):
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
                if self.model.Grid[row][col] != '':
                    text = self.font.render(self.model.Grid[row][col], True, (0, 0, 0))
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

    def draw_winner(self, player):
        if self.model.check_winner():
            text = self.font.render('wins!', True, (255, 0, 0))
            self.screen.blit(text, (self.size // 2 - text.get_width() // 2, self.size // 2 - text.get_height() // 2))
        elif self.model.is_draw():
            text = self.font.render('Draw!', True, (255, 0, 0))
            self.screen.blit(text, (self.size // 2 - text.get_width() // 2, self.size // 2 - text.get_height() // 2))

    def handle_click(self, pos):
        # if not self.model.is_draw():
        #     row, col = pos[1] // self.cell_size, pos[0] // self.cell_size
        #     self.model.make_move(row, col)
        root_player_1 = NodeMinMax(self.model.Grid, 'O', self.model.size_of_win)
        self.model.Grid = min_max(root_player_1, 1)

        self.draw_winner("1")  # TODO: il faut qu'on vérifie le winner après chaque coup d'un joueur

        # fonction node min max
        root_player_2 = NodeMinMax(self.model.Grid, 'X', self.model.size_of_win)
        self.model.Grid = min_max(root_player_2, 2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())

            self.draw_board()
            self.draw_winner(2)
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()
