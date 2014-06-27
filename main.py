import interface
import scene
from keys import load_bindings, bindings
from startscene import StartScene

def main():
    display = interface.Interface()
    load_bindings()
    current_scene = None

    def switch_scene(scene):
        current_scene = scene

    current_scene = StartScene(display)
    key = None
    while key != 'QUIT' and current_scene.game_over != True:
        key = display.get_input()
        if key in bindings:
            key = bindings[key]
        else:
            key = None
        current_scene.update(display, key)
        if current_scene.next_scene != None:
            current_scene = current_scene.next_scene
    display.__uninit__()

if __name__ == "__main__":
    main()
