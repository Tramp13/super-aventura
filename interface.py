import curses
from keys import load_bindings, bindings

BLACK = curses.COLOR_BLACK
RED = curses.COLOR_RED
GREEN = curses.COLOR_GREEN
YELLOW = curses.COLOR_YELLOW
BLUE = curses.COLOR_BLUE
MAGENTA = curses.COLOR_MAGENTA
CYAN = curses.COLOR_CYAN
WHITE = curses.COLOR_WHITE
TRANSPARENT = 9

def string_to_color(color_string):
    if color_string == 'BLACK':
        return BLACK
    elif color_string == 'RED':
        return RED
    elif color_string == 'GREEN':
        return GREEN
    elif color_string == 'YELLOW':
        return YELLOW
    elif color_string == 'BLUE':
        return BLUE
    elif color_string == 'MAGENTA':
        return MAGENTA
    elif color_string == 'CYAN':
        return CYAN
    elif color_string == 'WHITE':
        return WHITE
    elif color_string == 'TRANSPARENT':
        return TRANSPARENT
    else:
        return 0

def get_color_pair(fg, bg):
    return fg + (bg * 8) + 1

class Interface(object):
    def __init__(self, stdscr = None):
        if (stdscr == None):
            self.stdscr = curses.initscr()
        else:
            self.stdscr = stdscr
        curses.start_color()
        for bg in range(0, 8):
            for fg in range(0, 8):
                curses.init_pair(get_color_pair(fg, bg), fg, bg)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(True)
        load_bindings()

    def put_char(self, x, y, char, fg, bg, bold = False):
        attribute = curses.color_pair(get_color_pair(fg, bg))
        if bold:
            attribute |= curses.A_BOLD
        try:
            self.stdscr.addch(y, x, char, attribute)
        except curses.error:
            print("error in put_char")
            print(curses.error)

    def put_string(self, x, y, string, fg, bg, bold = False):
        for char in string:
            self.put_char(x, y, char, fg, bg, bold)
            x += 1

    def flush(self):
        self.stdscr.refresh()

    def clear(self):
        self.stdscr.clear()

    def clear_line(self, y):
        self.stdscr.move(y, 0)
        self.stdscr.clrtoeol()

    def get_input(self):
        key = self.stdscr.getkey()
        if key in bindings:
            return bindings[key]
        else:
            return None

    def get_size(self):
        height, width = self.stdscr.getmaxyx()
        return (width, height)

    def __uninit__(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
