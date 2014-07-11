from sprite import Sprite
import directions

RAW = 0
COOKED = 1
BURNT = 2

class Entity(object):
    def __init__(self, x, y, name, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.solid = True
        self.facing = directions.NORTH
        self.cooked = RAW
        self.cookable = False
        self.edible = False
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

    def drop(self, index):
        item = self.inventory.pop(index)
        item.x = self.x
        item.y = self.y
        return item

    def pickup(self, item):
        self.inventory.append(item)

    def cook(self):
        if self.cookable == False:
            return False
        if self.cooked == RAW:
            self.name = 'cooked ' + self.name
            self.cooked = COOKED
            return True
        if self.cooked == COOKED:
            self.cooked = BURNT
            self.name = 'burnt ' + self.name
            return True
        if self.cooked == BURNT:
            return False
