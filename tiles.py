from entity import Entity
from sprite import Sprite
from items import Fish, Log
import interface
import random

class Water(Entity):
    def __init__(self, x, y):
        sprite = Sprite('~', interface.BLUE, interface.BLACK, False)
        self.disturbed = False
        self.has_fish = True
        super(Water, self).__init__(x, y, 'water', sprite)

    def fish(self):
        self.disturbed = True
        if (self.has_fish):
            self.has_fish = False
            return Fish()
        else:
            return None

    def update(self):
        if (self.disturbed):
            self.sprite.bold = False
            self.sprite.fg = interface.WHITE
            self.disturbed = False
            return
        else:
            self.sprite.fg = interface.BLUE
        self.has_fish = True if random.random() < .05 else False
        if (self.has_fish):
            self.sprite.bold = True
        else:
            self.sprite.bold = False

class Tree(Entity):
    def __init__(self, x, y):
        sprite = Sprite('T', interface.GREEN, interface.BLACK, False)
        self.chopped = False
        self.ticks_since_chopped = 0
        super(Tree, self).__init__(x, y, 'tree', sprite)

    def chop(self):
        if (self.chopped == False):
            sprite = Sprite('.', interface.GREEN, interface.BLACK, False)
            self.chopped = True
            self.solid = False
            self.sprite = sprite
            return Log()
        else:
            return None

    def grow(self):
        sprite = Sprite('T', interface.GREEN, interface.BLACK, False)
        self.chopped = False
        self.ticks_since_chopped = 0
        self.solid = True
        self.sprite = sprite

    def update(self):
        if (self.chopped):
            self.ticks_since_chopped += 1
            if (self.ticks_since_chopped > 30):
                self.grow()

class Fire(Entity):
    def __init__(self, x, y):
        sprite = Sprite('&', interface.YELLOW, interface.BLACK, False)
        self.colors = [interface.YELLOW, interface.RED]
        super(Fire, self).__init__(x, y, 'fire', sprite)

    def update(self):
        self.sprite.fg = random.choice(self.colors)
