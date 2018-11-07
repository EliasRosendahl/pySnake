from snakepart import Snakepart




class Snake(object):
    def __init__(self):
        self.direction_x = 1
        self.direction_y = 0
        self.alive = True
        self.head = Snakepart(20, 0)
        self.parts = []

    def eat(self ,special=None):
        if special is None:
            self.parts.append(Snakepart(0, 0))


    def setDirection(self, x, y):
        self.direction_x = x
        self.direction_y = y

    def move(self):
        next_x = self.head.x
        next_y = self.head.y

        self.head.x += self.direction_x
        self.head.y += self.direction_y

        for part in self.parts:
            # sets last x and y to current position
            last_x = part.x
            last_y = part.y

            # Moves to next position
            part.x = next_x
            part.y = next_y

            # sets target for next snakepart
            next_x = last_x
            next_y = last_y 