from snake import Snake


class Model(object):
    def __init__(self):
        self.snake = Snake()

    def update(self):
        self.snake.move()