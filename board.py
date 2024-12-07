from cell import *
from sudoku_generator import generate_sudoku
from sudoku_generator import SudokuGenerator
import pygame


def valid_in_box(board, row_start, col_start, num):
    count = 0
    for i in range(0, 3):
        if board[row_start + i][col_start] == num:
            if count >1:
                return False
            count +=1
        for j in range(0, 3):
            if board[row_start + i][col_start + j] == num:
                if count >1:
                    return False
                count +=1
    return True

def valid_in_col(board, col, num):
    count = 0
    for row in range(9):
        if board[row][col] == num:
            if count > 1:
                return False
            count +=1
    return True

def valid_in_row(board, row, num):
    count = 0
    for number in board[row]:
        if num == number:
            count +=1
        if count > 1:
            return False
    return True

def is_valid(board, row, col, num):
    if not valid_in_row(board, row, num) or not valid_in_col(board, col, num) :
        return False

    if 0 < row <= 2:
        row = 0
    elif 3 < row <= 5:
        row = 3
    elif 6 < row <= 8:
        row = 6

    if 0 < col <= 2:
        col = 0
    elif 3 < col <= 5:
        col = 3
    elif 6 < col <= 9:
        col = 6


    if not valid_in_box(board,row, col, num):
        return False

    return True

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
            board_choice = generate_sudoku(9, 1)
        elif difficulty == 'medium':
            board_choice = generate_sudoku(9, 40)
        elif difficulty == 'hard':
            board_choice = generate_sudoku(9, 50)

        for row in range(9):
            for col in range(9):
                self.board[row][col].set_cell_value(board_choice[row][col])
        self.initial_board = board_choice

    def draw(self):
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
        temp_board = [[0 for x in range(9)] for y in range(9)]
        for row in range(9):
            for col in range(9):
                temp_board[row][col] = int(self.board[row][col].value)

        for row in range(9):
            for col in range(9):
                if not is_valid(temp_board, row, col, int(self.board[row][col].value)):
                    return False
        return True

