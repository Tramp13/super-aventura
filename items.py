from entity import Entity
from sprite import Sprite
import interface

class Fish(Entity):
    def __init__(self):
        sprite = Sprite.get('FISH')
        super(Fish, self).__init__(0, 0, 'fish', sprite)
        self.cookable = True
        self.edible = True

class Log(Entity):
    def __init__(self):
        sprite = Sprite.get('LOG')
        super(Log, self).__init__(0, 0, 'log', sprite)

class TinderBox(Entity):
    def __init__(self):
        sprite = Sprite.get('TINDER_BOX')
        super(TinderBox, self).__init__(0, 0, 'tinder box', sprite)

class Axe(Entity):
    def __init__(self):
        sprite = Sprite.get('AXE')
        super(Axe, self).__init__(0, 0, 'axe', sprite)

class FishingRod(Entity):
    def __init__(self):
        sprite = Sprite.get('FISHING_ROD')
        super(FishingRod, self).__init__(0, 0, 'fishing rod', sprite)
