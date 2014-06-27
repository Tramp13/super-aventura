from scene import Scene
from tilemap import Tilemap
from player import Player
from tiles import Water, Tree
import interface
import directions
import keys
from camera import Camera
import curses

class PlayScene(Scene):
    def draw_frame(self, display):
        width, height = display.get_size()
        fg = interface.WHITE
        bg = interface.BLACK
        for i in range(width):
            display.put_char(i, 0, curses.ACS_HLINE, fg, bg)
            display.put_char(i, 16, curses.ACS_HLINE, fg, bg)
            display.put_char(i, height - 1, curses.ACS_HLINE, fg, bg)
        for i in range(height):
            display.put_char(0, i, curses.ACS_VLINE, fg, bg)
            display.put_char(width - 1, i, curses.ACS_VLINE, fg, bg)
        for i in range(16):
            display.put_char(36, i, curses.ACS_VLINE, fg, bg)

        display.put_char(0, 0, curses.ACS_ULCORNER, fg, bg)
        display.put_char(36, 0, curses.ACS_TTEE, fg, bg)
        display.put_char(0, 16, curses.ACS_LTEE, fg, bg)
        display.put_char(36, 16, curses.ACS_BTEE, fg, bg)
        display.put_char(0, height - 1, curses.ACS_LLCORNER, fg, bg)
        display.put_char(width - 1, height - 1, curses.ACS_LRCORNER, fg, bg)
        display.put_char(width - 1, 0, curses.ACS_URCORNER, fg, bg)
        display.put_char(width, - 1, 16, curses.ACS_RTEE, fg, bg)

    def draw_tile(self, x, y, display):
        display_x = (x - self.camera.x) + 1
        display_y = (y - self.camera.y) + 1
        sprite = self.tilemap.get(x, y).sprite
        display.put_char(display_x,
                         display_y,
                         sprite.char,
                         sprite.fg,
                         sprite.bg,
                         sprite.bold)

    def draw_entity(self, entity_id, display):
        x = (self.entities[entity_id].x - self.camera.x) + 1
        y = (self.entities[entity_id].y - self.camera.y) + 1
        sprite = self.entities[entity_id].sprite
        display.put_char(x, y, sprite.char, sprite.fg, sprite.bg, sprite.bold)

    def print_log(self, display):
        width, height = display.get_size()
        for y in range(17, height - 1):
            for x in range(1, width - 1):
                display.put_char(x, y, ' ', 0, 0)
        for i in range(17, height - 1):
            if (len(self.log_messages) > i - 17):
                color = interface.BLACK
                if i == 17:
                    color = interface.WHITE
                display.put_string(1,
                                   i,
                                   self.log_messages[i - 17],
                                   color,
                                   interface.BLACK,
                                   False if i == 17 else True)

    def log(self, text):
        self.log_messages.insert(0, text)

    def __init__(self, display):
        super(PlayScene, self).__init__(display)
        display.clear()
        self.log_messages = []
        self.tilemap = Tilemap('map.txt')
        self.draw_frame(display)
        self.camera = Camera(35, 15, self.tilemap.width, self.tilemap.height)
        for y in range(self.camera.y, self.camera.y + self.camera.height):
            for x in range(self.camera.x, self.camera.x + self.camera.width):
                self.draw_tile(x, y, display)

        self.player = Player(self.camera.half_width, self.camera.half_height)
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

        self.camera.center_on(self.player.x, self.player.y)
        for y in range(self.camera.y, self.camera.y + self.camera.height):
            for x in range(self.camera.x, self.camera.x + self.camera.width):
                self.tilemap.get(x, y).update()
                self.draw_tile(x, y, display)


        self.draw_entity(self.player_id, display)

        self.print_log(display)

        display.flush()
