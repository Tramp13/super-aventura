from scene import Scene
from tilemap import Tilemap
from player import Player
from tiles import Water, Tree, Fire
from items import Log, TinderBox
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

    def draw_view(self, display):
        for i in self.camera:
            self.draw_tile(i.x, i.y, display)

    def update_and_draw_view(self, display):
        for i in self.camera:
            self.tilemap.get(i.x, i.y).update()
            self.draw_tile(i.x, i.y, display)
                

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

    def draw_inventory(self, display):
        width, height = display.get_size()
        for y in range(1, 16):
            for x in range(37, width - 1):
                display.put_char(x, y, ' ', 0, 0)
        for i in range(len(self.player.inventory)):
            name = self.player.inventory[i].name
            pos = i + 1
            display.put_string(39, pos, name, interface.WHITE, interface.BLACK)

    def select_item(self, display):
        fg = interface.WHITE
        bg = interface.BLACK
        selection = 0
        display.put_char(37, selection + 1, '>', fg, bg)
        display.flush()
        while True:
            key = display.get_input()
            display.put_char(37, selection + 1, ' ', 0, 0)
            if key == 'UP':
                selection -= 1
                if selection < 0:
                    selection = len(self.player.inventory) - 1
            if key == 'DOWN':
                selection += 1
                if selection >= len(self.player.inventory):
                    selection = 0
            if key == 'SELECT':
                break
            if key == 'q':
                return
            display.put_char(37, selection + 1, '>', fg, bg)
            display.flush()
        return selection

    def __init__(self, display):
        super(PlayScene, self).__init__(display)
        display.clear()
        self.log_messages = []
        self.tilemap = Tilemap()
        self.draw_frame(display)
        self.camera = Camera(35, 15, self.tilemap.width, self.tilemap.height)

        self.draw_view(display)

        self.player = Player(self.camera.half_width, self.camera.half_height)
        self.player_id = 0
        self.entities = [self.player]
        self.draw_entity(0, display)
        self.draw_inventory(display)
        display.flush()

    def update(self, display, key):
        if key == 'RESIZE':
            display.clear()
            self.draw_frame(display)
            self.draw_view(display)
            return
        #if key == 'APPLY':
        #    self.log('Apply what? (Directional keys to select.)')
        #    self.print_log(display)
            
        if key == 'DROP':
            self.log('Drop what? (Directional keys to select.)')
            self.print_log(display)
            item = self.player.drop(self.select_item(display))
            self.entities.insert(0, item)
            self.log('You drop the ' + item.name + '.')
            self.draw_inventory(display)
            self.print_log(display)
            return
        if key == 'APPLY':
            self.log('Apply what? (Directional keys to select.)')
            self.print_log(display)
            item = self.player.inventory[self.select_item(display)]
            self.log('Apply ' + item.name + ' in which direction?')
            self.print_log(display)
            direction = directions.from_key(display.get_input())
            if direction != directions.INVALID:
                delta_x, delta_y = directions.delta(direction)
                tile_x = self.player.x + delta_x
                tile_y = self.player.y + delta_y
                for i in self.entities:
                    if i.x == tile_x and i.y == tile_y:
                        if type(i) == Log and type(item) == TinderBox:
                            self.entities.remove(i)
                            self.tilemap.set(tile_x,
                                             tile_y,
                                             Fire(tile_x, tile_y))
                            self.draw_tile(tile_x, tile_y, display)
                            self.log('You make a fire')
                            self.print_log(display)
                            break

            else:
                self.log('Uh, that\'s not a direction')
                self.print_log(display)
            return
            
        direction = directions.from_key(key)
        if direction != directions.INVALID:
            self.player.move(direction)
            tile = self.tilemap.get(self.player.x, self.player.y)

            if tile.solid:
                self.player.move_back()
            
            if type(tile) == Water:
                fish = tile.fish()
                if fish != None:
                    self.log('You catch a fish!')
                    self.player.inventory.append(fish)
                else:
                    self.log('You disturb the water.')

            if type(tile) == Tree:
                log = tile.chop()
                if log != None:
                    self.log('You cut down the tree, and aquire some logs')
                    self.player.inventory.append(log)

        self.camera.center_on(self.player.x, self.player.y)
        self.update_and_draw_view(display)

        for i in range(len(self.entities)):
            self.draw_entity(i, display)
        self.draw_inventory(display)

        self.print_log(display)

        display.flush()
