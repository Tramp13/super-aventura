from sprite import Sprite
import directions

class Entity(object):
    def __init__(self, x, y, name, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.solid = True
        self.facing = directions.NORTH
        self.inventory = []

    def update(self):
        pass

    def move(self, direction):
        self.facing = direction
        x_delta, y_delta = directions.delta(direction)
        self.x += x_delta
        self.y += y_delta

    def move_back(self):
        x_delta, y_delta = directions.delta(directions.reverse(self.facing))
        self.x += x_delta
        self.y += y_delta

    def lose(self, index):
        return self.inventory.pop(index)
