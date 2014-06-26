from scene import Scene
from tilemap import Tilemap
from player import Player
from tiles import Water, Tree
import interface
import directions
import keys

class PlayScene(Scene):
    def draw_tile(self, x, y, display):
        sprite = self.tilemap.get(x, y).sprite
        display.put_char(x, y, sprite.char, sprite.fg, sprite.bg, sprite.bold)

    def draw_entity(self, entity_id, display):
        x = self.entities[entity_id].x
        y = self.entities[entity_id].y
        sprite = self.entities[entity_id].sprite
        display.put_char(x, y, sprite.char, sprite.fg, sprite.bg, sprite.bold)

    def print_log(self, display):
        display.clear_line(15)
        display.clear_line(16)
        if (len(self.log_messages) > 0):
            display.put_string(0,
                               15,
                               self.log_messages[0],
                               interface.WHITE,
                               interface.BLACK)
        if (len(self.log_messages) > 1):
            display.put_string(0,
                               16,
                               self.log_messages[1],
                               interface.BLACK,
                               interface.BLACK,
                               True)

    def log(self, text):
        self.log_messages.insert(0, text)

    def __init__(self, display):
        super(PlayScene, self).__init__(display)
        display.clear()
        self.log_messages = []
        self.tilemap = Tilemap('map.txt')
        for y in range(self.tilemap.height):
            for x in range(self.tilemap.width):
                self.draw_tile(x, y, display)

        self.player = Player(1, 1)
        self.player_id = 0
        self.entities = [self.player]
        self.draw_entity(0, display)
        display.flush()

    def update(self, display, key):
        direction = directions.from_key(key)
        if (direction != directions.INVALID):
            self.player.move(direction)
            tile = self.tilemap.get(self.player.x, self.player.y)

            if (tile.solid):
                self.player.move_back()
            
            if (type(tile) == Water):
                fish = tile.fish()
                if fish != None:
                    self.log('You catch a fish!')
                    self.player.inventory.append(fish)
                else:
                    self.log('You disturb the water.')

            if (type(tile) == Tree):
                log = tile.chop()
                if log != None:
                    self.log('You cut down the tree, and aquire some logs')
                    self.player.inventory.append(log)


        for y in range(self.tilemap.height):
            for x in range(self.tilemap.width):
                self.tilemap.get(x, y).update()
                self.draw_tile(x, y, display)


        self.draw_entity(self.player_id, display)

        self.print_log(display)

        display.flush()
