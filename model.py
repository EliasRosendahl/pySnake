import random

from snake import Snake
from food import Food

class Model(object):
    def __init__(self):
        self.snake = Snake()
        self.food = [Food(10, 10)]

    def update(self):
        for food in self.food:
            if self.snake.head.x == food.x and self.snake.head.y == food.y:
                self.food.remove(food)
                self.food.append(Food(random.randrange(20), random.randrange(20)))
                self.snake.eat()
                break
        self.snake.move()