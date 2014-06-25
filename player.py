from entity import Entity
from sprite import Sprite
import interface

class Player(Entity):
    def __init__(self, x, y):
        sprite = Sprite('@', interface.WHITE, interface.BLACK, False)
        super(Player, self).__init__(x, y, 'player', sprite)
