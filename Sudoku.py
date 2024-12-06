import pygame
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

def gamestart():
    print("start game")
def gameover():
    print("game over")

def gameloop():

    width = 729
    height = 900
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))

    board = Board(width, height, screen, "easy")
    board.draw()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()


        pygame.display.flip()



gameloop()