from sprite import Sprite
from entity import Entity
from tiles import Water, Tree
import interface

def char_to_entity(x, y, char):
    sprite = None
    solid = None
    name = None
    if (char == 'T'):
        return Tree(x, y)
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

    def get_x(self, x):
        if x < 0:
            return self.get_x(x + self.width)
        elif x >= self.width:
            return self.get_x(x - self.width)
        else:
            return x

    def get_y(self, y):
        if y < 0:
            return self.get_y(y + self.height)
        elif y >= self.height:
            return self.get_y(y - self.height)
        else:
            return y

    def get(self, x, y):
        #new_x = self.get_x(x)
        #new_y = self.get_y(y)
        return self.tiles[y][x]
