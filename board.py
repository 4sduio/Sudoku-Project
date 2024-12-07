from cell import *
from sudoku_generator import generate_sudoku
import pygame

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected = None
        self.initial_board = []
        if difficulty == 'easy':
            board_choice = generate_sudoku(9, 30)
        elif difficulty == 'medium':
            board_choice = generate_sudoku(9, 40)
        elif difficulty == 'hard':
            board_choice = generate_sudoku(9, 50)

        for row in range(9):
            for col in range(9):
                self.board[row][col].set_cell_value(board_choice[row][col])
        self.initial_board = board_choice

    def draw(self):
        self.screen.fill((255, 255, 255))
        square_size = self.width / 9
        for row in range(10):
            if row % 3 == 0:
                line_width = 5
            else:
                line_width = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * square_size), (self.width, row * square_size),
                             line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (row * square_size, 0), (row * square_size, self.width),
                             line_width)
        for row in range(9):
            for col in range(9):
                self.board[row][col].draw()
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (self.selected[1] * square_size, self.selected[0] * square_size, square_size, square_size),
                             3)
        pygame.display.update()

    def select(self, row, col):
        self.selected = (row, col)

    def click(self, x, y):
        square_size = self.width / 9
        row = int(x // square_size)
        col = int(y // square_size)

        return row, col

    def clear(self):
        if self.selected:
            row, col = self.selected
            if self.initial_board[row][col] == 0:
                self.board[row][col].set_cell_value(0)
                self.board[row][col].draw()

    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            self.board[row][col].set_sketched_value(value)

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            if self.board[row][col].value == 0:
                self.board[row][col].set_cell_value(value)
                self.board[row][col].set_sketched_value(0)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col].set_cell_value(self.initial_board[row][col])
                self.board[row][col].set_sketched_value(0)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col].get_cell_value() == 0:
                    return False
        return True

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col].set_cell_value()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col].get_cell_value() == 0:
                    return(row, col)
        return None

    def check_board(self):
        for row in range(9):
            for col in range(9):
                value = self.board[row][col].get_cell_value()
                if not self.sudoku_generator.is_valid(row, col, value):
                    return False
        return True

