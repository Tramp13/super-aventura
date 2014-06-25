from entity import Entity
from sprite import Sprite
from items import Fish
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
