from sprite import Sprite
from entity import Entity
from tiles import Water, Tree, Wheat
from chicken import Chicken
import interface
import os

default_map = '''43>
18>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~...T..........~~~~~.....T.....~~......~~~
~~...........TT........T...........T....~~~
~~..."".......T..........T.........."..~~~~
~~~.."""...............................~~~~
~~~...............c.....................~~~
~~.........TT.................TTT........~~
~~..T...........T....""".................~~
~~..............T...."""............T....~~
~~......."...............................~~
~~~..T.................TT................~~
~~~.................................""...~~
~~.........................T......T......~~
~~........T...T.........T........T......T~~
~~.......................................~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

class Tilemap(object):
    def __init__(self):
        if (os.path.isdir(os.path.expanduser('~/.adventure')) == False):
            os.makedirs(os.path.expanduser('~/.adventure'))
        if (os.path.exists(os.path.expanduser('~/.adventure/map.txt')) ==
                           False):
            map_file = open(os.path.expanduser('~/.adventure/map.txt'), 'w')
            map_file.write(default_map)
            map_file.close()

        data_file = open(os.path.expanduser('~/.adventure/map.txt'), 'r')
        [width, height, data] = data_file.read().split('>\n')
        self.width = int(width)
        self.height = int(height)
        self.entities = []
        self.tiles = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                tile = self.char_to_entity(x, y, data[(y * self.width) + x + y])
                self.tiles.append(tile)
        data_file.close()

    def char_to_entity(self, x, y, char):
        sprite = None
        solid = None
        name = None
        if (char == 'T'):
            return Tree(x, y)
        if (char == '.'):
            sprite = Sprite.get('GRASS')
            solid = False
            name = 'grass'
        if (char == 'c'):
            sprite = Sprite.get('GRASS')
            solid = False
            name = 'grass'
            self.entities.append(Chicken(x, y))
        if (char == '~'):
            return Water(x, y)
        if (char == '"'):
            return Wheat(x, y)
        entity = Entity(x, y, name, sprite)
        entity.solid = solid
        return entity

    def get(self, x, y):
        return self.tiles[(y * self.width) + x]

    def set(self, x, y, tile):
        self.tiles[(y * self.width) + x] = tile

    def __iter__(self):
        return iter(self.tiles)
