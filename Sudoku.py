
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
screen.fill((255,255,255))

def game_start():

    running = True
    while running:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            title_font = pygame.font.Font(None, 100)
            font = pygame.font.SysFont(None, 70)
            title_surface = title_font.render('Sudoku', True, (0, 0, 0))
            title_rect = title_surface.get_rect(center=(WIDTH / 2, 200))
            screen.blit(title_surface, title_rect)

            title_font = pygame.font.Font(None, 80)

            game_mode_surface = title_font.render('Select Game mode :', True, (0, 0, 0))
            game_mode_rect = game_mode_surface.get_rect(center=(WIDTH / 2, 450))
            screen.blit(game_mode_surface, game_mode_rect)


            easy_button_text = font.render('Easy', True, (255, 255, 255))
            medium_button_text = font.render('Medium', True, (255, 255, 255))
            hard_button_text = font.render('Hard', True, (255, 255, 255))

            easy_button = pygame.Surface((easy_button_text.get_size()[0] + 20, easy_button_text.get_size()[1] + 20))
            easy_button.fill((0, 0, 0))
            easy_button.blit(easy_button_text, (10, 10))

            medium_button = pygame.Surface(
                (medium_button_text.get_size()[0] + 20, medium_button_text.get_size()[1] + 20))
            medium_button.fill((0, 0, 0))
            medium_button.blit(medium_button_text, (10, 10))

            hard_button = pygame.Surface((hard_button_text.get_size()[0] + 20, hard_button_text.get_size()[1] + 20))
            hard_button.fill((0, 0, 0))
            hard_button.blit(hard_button_text, (10, 10))

            easy_button_rect = easy_button.get_rect(center=(WIDTH / 5, 600))
            medium_button_rect = medium_button.get_rect(center=(WIDTH / 2, 600))
            hard_button_rect = hard_button.get_rect(center=(WIDTH * (4 / 5), 600))

            screen.blit(easy_button, easy_button_rect)
            screen.blit(medium_button, medium_button_rect)
            screen.blit(hard_button, hard_button_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return 'easy'
                elif medium_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return 'medium'
                elif hard_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return 'hard'
                pass
        pygame.display.update()
        clock.tick(60)

def game_won():

    screen.fill((255,255,255))

    running = True
    while running:

        screen.fill((255, 255, 255))
        running = True
        while running:
            clock = pygame.time.Clock()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                title_font = pygame.font.Font(None, 100)
                font = pygame.font.SysFont(None, 70)
                title_surface = title_font.render('Game Won!', True, (0, 0, 0))
                title_rect = title_surface.get_rect(center=(WIDTH / 2, 200))
                screen.blit(title_surface, title_rect)
                pygame.display.update()

                button_text = font.render('Exit', True, (255, 255, 255))

                button = pygame.Surface((button_text.get_size()[0] + 20, button_text.get_size()[1] + 20))
                button.fill((0, 0, 0))
                button.blit(button_text, (10, 10))

                button_rect = button.get_rect(center=(WIDTH / 2, 480))
                screen.blit(button, button_rect)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()

            pygame.display.update()
            clock.tick(60)

def game_lost():
    screen.fill((255, 255, 255))

    running = True
    while running:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            title_font = pygame.font.Font(None, 100)
            font = pygame.font.SysFont(None, 70)
            title_surface = title_font.render('Game Over :(', True, (0, 0, 0))
            title_rect = title_surface.get_rect(center=(WIDTH / 2, 200))
            screen.blit(title_surface, title_rect)
            pygame.display.update()

            button_text = font.render('Restart', True, (255, 255, 255))

            button = pygame.Surface((button_text.get_size()[0] + 20, button_text.get_size()[1] + 20))
            button.fill((0, 0, 0))
            button.blit(button_text, (10, 10))

            button_rect = button.get_rect(center=(WIDTH / 2, 480))
            screen.blit(button, button_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    return

        pygame.display.update()
        clock.tick(60)

def main():

    running = True

    clock = pygame.time.Clock()
    while running:

        screen.fill((255, 255, 255))
        difficulty = game_start()
        board = Board(WIDTH, HEIGHT, screen, difficulty)
        font = pygame.font.SysFont(None, 50)
        reset_button_text = font.render('Reset', True, (255,255,255))
        restart_button_text = font.render('Restart', True, (255,255,255))
        exit_button_text = font.render('Exit', True, (255,255,255))

        reset_button = pygame.Surface(
            (reset_button_text.get_size()[0] + 20, reset_button_text.get_size()[1] + 20))
        reset_button.fill((0, 0, 0))
        reset_button.blit(reset_button_text, (10, 10))

        restart_button = pygame.Surface(
            (restart_button_text.get_size()[0] + 20, restart_button_text.get_size()[1] + 20))
        restart_button.fill((0, 0, 0))
        restart_button.blit(restart_button_text, (10, 10))

        exit_button = pygame.Surface((exit_button_text.get_size()[0] + 20, exit_button_text.get_size()[1] + 20))
        exit_button.fill((0, 0, 0))
        exit_button.blit(exit_button_text, (10, 10))

        reset_button_rect = reset_button.get_rect(center=(WIDTH / 5, 850))
        restart_button_rect = restart_button.get_rect(center=(WIDTH / 2, 850))
        exit_button_rect = exit_button.get_rect(center=(WIDTH * (4 / 5), 850))

        white_square = pygame.Surface((729,729))
        white_square.fill((255, 255, 255))
        white_square_rect = white_square.get_rect(topleft=(0, 0))

        is_full = board.is_full()
        while not is_full:

            screen.blit(white_square, white_square_rect)

            board.draw()

            screen.blit(reset_button, reset_button_rect)
            screen.blit(restart_button, restart_button_rect)
            screen.blit(exit_button, exit_button_rect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = board.click(y, x)
                    if row < 9 and col < 9:
                        board.select(row, col)
                    if reset_button_rect.collidepoint(pygame.mouse.get_pos()):
                        board.reset_to_original()
                    elif restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                        is_full = True
                    elif exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()
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
                pygame.display.update()
                clock.tick(60)




        if board.is_full():
            if board.check_board():
                game_won()
            else:
                game_lost()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
if __name__ == '__main__':
    main()
