import pygame
from pygame.examples.scrap_clipboard import screen

pygame.init()

sketch = True

class Cell:

    def __init__(self,value,row,col,screen):
        self.screen = screen
        self.row = 81*(row-1)
        self.col = 81*(col-1)
        self.sketchedvalue = value

    def set_cell_value(self, value):
        sketch = False
        self.value = value

    def set_sketched_value(self, value):
        sketch = True
        self.sketchedvalue = value


    def draw(self):
        Square = pygame.Surface((78,78))
        Square.fill((255,255,255))
        outline = pygame.Surface((81,81))
        outline.fill('red')

        cell = Square.get_rect(center=((41+ self.row,41+self.col)))
        font = pygame.font.SysFont('comicsans', 30)

        self.screen.blit(outline, cell)
        self.screen.blit(Square, cell)
        if sketch:
            number = font.render(str(self.sketchedvalue), True, 'grey')
            if 9 >= self.sketchedvalue > 0:
                self.screen.blit(number, Square.get_rect(topleft=(self.row, self.col)))
        else:
            number = font.render(str(self.sketchedvalue), True, 'black')
            self.screen.blit(number, cell)





#
#
# def gameloop():
#     screen = pygame.display.set_mode((810,810))
#     screen.fill((255,255,255))
#     test = Cell(5,1,1,screen)
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 x,y = pygame.mouse.get_pos()
#                 if test.row< x < test.row +81 and test.col< y < test.col+81:
#                     test.draw()
#
#         pygame.display.flip()
# gameloop()