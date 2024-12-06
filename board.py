import pygame
from pygame.draw_py import draw_line
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:

    def __init__(self, Width, Height, Screen, difficulty):
        self.width = Width
        self.height = Height
        self.screen = Screen
        self.difficulty = difficulty
        if difficulty == 'easy':
            self.board = generate_sudoku(9, 30)
        elif difficulty == 'medium':
            self.board = generate_sudoku(9, 40)
        elif difficulty == 'hard':
            self.board = generate_sudoku(9, 50)


    def draw(self):
        self.screen.fill((255,255,255))
        for i in range(1, 10):
            if i == 3 or i == 6 or i == 9:
                draw_line(self.screen, ("black"), (81 * i, 0), (81 * i, 729), 5)
                draw_line(self.screen, ("black"), (0, 81 * i), (729, 81 * i), 5)
                pygame.display.flip()
            else:
                draw_line(self.screen, ("black"), (81 * i, 0), (81 * i, 729), 2)
                draw_line(self.screen, ("black"), (0, 81 * i), (729, 81 * i), 2)
                pygame.display.flip()



        for i in range(0, 9):
            for j in range(0, 9):
                self.board[i][j] = Cell(self.board[i][j],i,j,self.screen)

        for cell in self.board:
            cell.Cell.draw()

    def select(self, row, col):

    def clear(self):

    def sketch(self, value):

    def place_number(self, value):

    def reset_to_original(self):

    def is_full(self):

    def update_board(self):

    def find_empty(self):

    def check_board(self):

