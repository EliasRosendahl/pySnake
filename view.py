import pygame


class View(object):
    def __init__(self):
        pygame.init()

        size = (720, 480)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("snake")

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.PIXELSIZE = 16

    def update(self, model):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(
            model.snake.head.x * self.PIXELSIZE, 
            model.snake.head.y * self.PIXELSIZE, 
            self.PIXELSIZE, 
            self.PIXELSIZE))

        for part in model.snake.parts:
            pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(
                part.x * self.PIXELSIZE, 
                part.y * self.PIXELSIZE, 
                self.PIXELSIZE, 
                self.PIXELSIZE))

        pygame.display.flip()
