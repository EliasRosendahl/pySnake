import pygame


class View(object):
    def __init__(self):
        pygame.init()

        # Needs better way to store colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.PIXELSIZE = 16

        size = (45 * self.PIXELSIZE, 30 * self.PIXELSIZE)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("snake")

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

        for food in model.food:
            pygame.draw.rect(self.screen, self.RED, pygame.Rect(
                food.x * self.PIXELSIZE,
                food.y * self.PIXELSIZE,
                self.PIXELSIZE,
                self.PIXELSIZE))

        pygame.display.flip()
