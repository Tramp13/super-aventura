from entity import Entity
from sprite import Sprite
import interface

class Fish(Entity):
    def __init__(self):
        sprite = Sprite('%', interface.WHITE, interface.BLACK, True)
        super(Fish, self).__init__(0, 0, 'fish', sprite)
