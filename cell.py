import pygame

pygame.init()

sketch = True

class Cell:

    def __init__(self,value,row,col,screen):
        self.screen = screen
        self.row = row
        self.col = col
        self.sketched_value = 0
        self.value = value


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def get_cell_value(self):
        return self.value

    def draw(self):
        square_size = self.screen.get_width() // 9
        square = pygame.Rect(self.col * square_size, self.row * square_size, square_size, square_size)
        font = pygame.font.SysFont('comicsans', 30)
        pygame.draw.rect(self.screen, (0, 0, 0), square, 1)
        if self.sketched_value != 0:
            number = font.render(str(self.sketched_value), True, 'black')
            number_placement = number.get_rect(center = (self.col * square_size + square_size // 2, self.row * square_size + square_size //2))
            self.screen.blit(number, number_placement)












