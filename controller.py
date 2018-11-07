import pygame


class Controller(object):
    def __init__(self, view, model):
        self.view = view
        self. model = model
        self.clock = pygame.time.Clock()

    def run(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.model.snake.setDirection(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.model.snake.setDirection(1, 0)
                elif event.key == pygame.K_UP:
                    self.model.snake.setDirection(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.model.snake.setDirection(0, 1)
            
            self.model.update()
            self.view.update(self.model)
            self.clock.tick(60)
            
        pygame.quit()