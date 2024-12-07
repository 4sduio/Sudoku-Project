
import pygame
import random
from sudoku_generator import *
from board import *
from cell import *

WIDTH = 720
HEIGHT = 900
CELL_SIZE = 72

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

difficulty = 'medium'

def main():
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = board.click(y, x)
                if row < 9 and col < 9:
                    board.select(row, col)
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                                 pygame.K_8, pygame.K_9]:
                    if board.selected:
                        row, col = board.selected
                        value = event.key - pygame.K_0
                        board.board[row][col].set_sketched_value(value)
                elif event.key == pygame.K_RETURN:
                    if board.selected:
                        row, col = board.selected
                        value = board.board[row][col].sketched_value
                        if value != 0:
                            board.place_number(value)
                elif event.key == pygame.K_BACKSPACE:
                    if board.selected:
                        board.clear()
        board.draw()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
if __name__ == '__main__':
    main()
