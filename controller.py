import pygame


class Controller(object):
    def __init__(self, view, model):
        self.view = view
        self. model = model
        self.clock = pygame.time.Clock()
        self.move_delay = 50
        self.last_move = pygame.time.get_ticks()

    def run(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.model.snake.setDirection(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.model.snake.setDirection(1, 0)
                    elif event.key == pygame.K_UP:
                        self.model.snake.setDirection(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.model.snake.setDirection(0, 1)
            
            # Only moves if snake is still alive
            if self.model.snake.alive:
                if pygame.time.get_ticks() > self.last_move + self.move_delay:
                    self.model.update()
                    self.last_move = pygame.time.get_ticks()

            
            self.view.update(self.model)
            self.clock.tick(60)

        pygame.quit()