import curses

BLACK = curses.COLOR_BLACK
RED = curses.COLOR_RED
GREEN = curses.COLOR_GREEN
YELLOW = curses.COLOR_YELLOW
BLUE = curses.COLOR_BLUE
MAGENTA = curses.COLOR_MAGENTA
CYAN = curses.COLOR_CYAN
WHITE = curses.COLOR_WHITE

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

    def put_char(self, x, y, char, fg, bg, bold = False):
        attribute = curses.color_pair(get_color_pair(fg, bg))
        if bold:
            attribute |= curses.A_BOLD
        try:
            self.stdscr.addch(y, x, char, attribute)
        except curses.error:
            pass

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
        return self.stdscr.getkey()

    def get_size(self):
        height, width = self.stdscr.getmaxyx()
        return (width, height)

    def __uninit__(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
