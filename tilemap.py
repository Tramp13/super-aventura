from sprite import Sprite
from entity import Entity
from water import Water
import interface

def char_to_entity(x, y, char):
    sprite = None
    solid = None
    name = None
    if (char == 'T'):
        sprite = Sprite(char, interface.GREEN, interface.BLACK, False)
        solid = True
        name = 'tree'
    if (char == '.'):
        sprite = Sprite(char, interface.GREEN, interface.BLACK, False)
        solid = False
        name = 'grass'
    if (char == '~'):
        return Water(x, y)
    entity = Entity(x, y, name, sprite)
    entity.solid = solid
    return entity

class Tilemap(object):
    def __init__(self, filename):
        data_file = open(filename, 'r')
        [width, height, data] = data_file.read().split('>\n')
        self.width = int(width)
        self.height = int(height)
        self.tiles = []
        for y in range(0, self.height):
            self.tiles.append([])
            for x in range(0, self.width):
                tile = char_to_entity(x, y, data[(y * self.width) + x + y])
                self.tiles[y].append(tile)
        data_file.close()

    def get(self, x, y):
        return self.tiles[y][x]
