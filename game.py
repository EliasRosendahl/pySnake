import pygame

from snake import Snake

pygame.init()


size = (720, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("gotoFood")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PIXELSIZE = 16


done = False
clock = pygame.time.Clock()

snake = Snake()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake.setDirection(-1, 0)
        elif event.key == pygame.K_RIGHT:
            snake.setDirection(1, 0)
        elif event.key == pygame.K_UP:
            snake.setDirection(0, -1)
        elif event.key == pygame.K_DOWN:
            snake.setDirection(0, 1)

    snake.move()
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(
        snake.head.x * PIXELSIZE, 
        snake.head.y * PIXELSIZE, 
        PIXELSIZE, 
        PIXELSIZE))

    for part in snake.parts:
        pygame.draw.rect(screen, BLACK, pygame.Rect(
        part.x * PIXELSIZE, 
        part.y * PIXELSIZE, 
        PIXELSIZE, 
        PIXELSIZE))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()