from entity import Entity
from sprite import Sprite
from items import Fish, Log
import interface
import random

class Water(Entity):
    def __init__(self, x, y):
        self.disturbed = False
        self.has_fish = True
        super(Water, self).__init__(x, y, 'water', Sprite.get('WATER'))

    def fish(self):
        self.disturbed = True
        if (self.has_fish):
            self.has_fish = False
            return Fish()
        else:
            return None

    def disturb(self):
        self.disturbed = True

    def update(self):
        if (self.disturbed):
            self.sprite = Sprite.get('WATER_DISTURBED')
            self.disturbed = False
            return
        self.has_fish = True if random.random() < .05 else False
        if (self.has_fish):
            self.sprite = Sprite.get('WATER_ACTIVE')
        else:
            self.sprite = Sprite.get('WATER')

class Tree(Entity):
    def __init__(self, x, y):
        self.chopped = False
        self.ticks_since_chopped = 0
        super(Tree, self).__init__(x, y, 'tree', Sprite.get('TREE'))

    def chop(self):
        if (self.chopped == False):
            sprite = Sprite.get('GRASS')
            self.chopped = True
            self.solid = False
            self.sprite = sprite
            return Log()
        else:
            return None

    def grow(self):
        self.chopped = False
        self.ticks_since_chopped = 0
        self.solid = True
        self.sprite = Sprite.get('TREE')

    def update(self):
        if (self.chopped):
            self.ticks_since_chopped += 1
            if (self.ticks_since_chopped > 30):
                self.grow()

class Fire(Entity):
    def __init__(self, x, y):
        super(Fire, self).__init__(x, y, 'fire', Sprite.get('FIRE1'))

    def update(self):
        self.sprite.fg = random.choice([Sprite.get('FIRE1'),
                                        Sprite.get('FIRE2')])
