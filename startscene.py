from scene import Scene
from menu import Menu
from playscene import PlayScene
import interface

class StartScene(Scene):
    def __init__(self, display):
        super(StartScene, self).__init__(display)
        self.menu = Menu()
        def start_game():
            self.next_scene = PlayScene(display)

        def quit_game():
            display.put_string(10,
                               10,
                               "Ba",
                               interface.WHITE,
                               interface.BLACK,
                               False)

        self.menu.add_option(("Start", start_game))
        self.menu.add_option(("Quit", quit_game))

        for i in range(0, self.menu.length()):
            text, _ = self.menu.get(i)
            display.put_string(2,
                               i,
                               text,
                               interface.WHITE,
                               interface.BLACK,
                               False)

        display.put_char(0, 0, '>', interface.WHITE, interface.BLACK, True)

    def update(self, display, key):
        display.put_char(0,
                         self.menu.selection,
                         ' ',
                         interface.WHITE,
                         interface.BLACK,
                         False)
        if key == 'j':
            self.menu.select_next()
        if key == 'k':
            self.menu.select_previous()
        if key == 'x':
            _, callback = self.menu.get_selection()
            callback()
            return

        display.put_char(0,
                         self.menu.selection,
                         '>',
                         interface.WHITE,
                         interface.BLACK,
                         True)

        display.flush()
