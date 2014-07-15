from entity import Entity
from sprite import Sprite
from items import TinderBox
import interface

class Player(Entity):
    def __init__(self, x, y):
        sprite = Sprite.get('PLAYER')
        super(Player, self).__init__(x, y, 'player', sprite)
        self.inventory.append(TinderBox())
