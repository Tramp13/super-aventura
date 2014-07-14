#!/usr/bin/env python

import interface
import scene
import curses
from startscene import StartScene
from sprite import load_sprites

def main(stdscr):
    display = interface.Interface(stdscr)
    load_sprites()
    current_scene = None

    def switch_scene(scene):
        current_scene = scene

    current_scene = StartScene(display)
    key = None
    while key != 'QUIT' and current_scene.game_over != True:
        key = display.get_input()
        current_scene.update(display, key)
        if current_scene.next_scene != None:
            current_scene = current_scene.next_scene
    display.__uninit__()

if __name__ == "__main__":
    curses.wrapper(main)
