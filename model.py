import random

from snake import Snake
from food import Food

class Model(object):
    def __init__(self):
        self.snake = Snake()
        self.food = [Food(10, 10)]
        self.score = 0

    def update(self):
        # Checks if snake can eat the food
        for food in self.food:
            if self.snake.head.x == food.x and self.snake.head.y == food.y:
                self.food.remove(food)
                self.food.append(Food(random.randrange(20), random.randrange(20)))
                self.snake.eat()
                self.score += 1
                break

        self.snake.move()

        # Checks if snake has hit itself
        for part in self.snake.parts:
            if part.x == self.snake.head.x and part.y == self.snake.head.y:
                self.snake.alive = False