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

        self.font = pygame.font.SysFont("Sans Seriff", 42)

    def update(self, model):
        self.screen.fill(self.WHITE)

        # Draw snake head
        pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(
            model.snake.head.x * self.PIXELSIZE, 
            model.snake.head.y * self.PIXELSIZE, 
            self.PIXELSIZE, 
            self.PIXELSIZE))

        # Draw snake body
        for part in model.snake.parts:
            pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(
                part.x * self.PIXELSIZE, 
                part.y * self.PIXELSIZE, 
                self.PIXELSIZE, 
                self.PIXELSIZE))

        # Draw food
        for food in model.food:
            pygame.draw.rect(self.screen, self.RED, pygame.Rect(
                food.x * self.PIXELSIZE,
                food.y * self.PIXELSIZE,
                self.PIXELSIZE,
                self.PIXELSIZE))

        # Show score
        if model.snake.alive:
            scoreString = "Score: " + str(model.score)
        else:
            scoreString = "Game over! Score: " + str(model.score)
        scoreText = self.font.render(scoreString, True, (0, 128, 0))
        self.screen.blit(scoreText, (0, 0))

        pygame.display.flip()
