import os
from interface import string_to_color

default_sprites = '''PLAYER @ WHITE BLACK FALSE
WATER ~ BLUE BLACK FALSE
WATER_DISTURBED ~ WHITE BLACK FALSE
WATER_ACTIVE ~ BLUE BLACK TRUE
GRASS . GREEN BLACK FALSE
TREE T GREEN BLACK FALSE
FIRE1 & YELLOW BLACK FALSE
FIRE2 & RED BLACK FALSE
FISH % WHITE BLACK FALSE
TINDER_BOX [ WHITE BLACK FALSE
FISHING_ROD [ WHITE BLACK FALSE
AXE / WHITE BLACK FALSE
LOG x WHITE BLACK FALSE
WHEAT " YELLOW BLACK FALSE
CHICKEN c WHITE BLACK FALSE'''

sprites = {}

class Sprite:
    def __init__(self, char, fg, bg, bold):
        self.char = char
        self.fg = fg
        self.bg = bg
        self.bold = bold
    def get(name):
        return sprites[name]
    get = staticmethod(get)

def load_sprites():
    if os.path.isdir(os.path.expanduser('~/.adventure')) == False:
        os.makedirs(os.path.expanduser('~/.adventure'))
    if os.path.exists(os.path.expanduser('~/.adventure/sprites.txt')) == False:
        sprites_file = open(os.path.expanduser('~/.adventure/sprites.txt'), 'w')
        sprites_file.write(default_sprites)
        sprites_file.close()

    sprites_file = open(os.path.expanduser('~/.adventure/sprites.txt'), 'r')
    sprites_data = sprites_file.read().split('\n')
    for i in sprites_data:
        sprite_data = i.split(' ')
        if len(sprite_data) < 2:
            continue
        name = sprite_data[0]
        char = sprite_data[1]
        fg = string_to_color(sprite_data[2])
        bg = string_to_color(sprite_data[3])
        bold = True if sprite_data[4] == 'TRUE' else False
        sprites[name] = Sprite(char, fg, bg, bold)

