class Menu:
    def __init__(self):
        self.options = []
        self.selection = 0

    def add_option(self, option):
        self.options.append(option)

    def select_next(self):
        self.selection += 1
        if (self.selection >= len(self.options)):
            self.selection = 0

    def select_previous(self):
        self.selection -= 1
        if (self.selection < 0):
            self.selection = len(self.options) - 1

    def get(self, index):
        return self.options[index]

    def get_selection(self):
        return self.options[self.selection]

    def length(self):
        return len(self.options)
