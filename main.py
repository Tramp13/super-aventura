import interface
import scene
import keys
from startscene import StartScene

def main():
    display = interface.Interface()
    current_scene = None

    def switch_scene(scene):
        current_scene = scene

    current_scene = StartScene(display)
    key = None
    while key != keys.QUIT:
        key = display.get_input()
        if key in keys.bindings:
            key = keys.bindings[key]
        else:
            key = None
        current_scene.update(display, key)
        if current_scene.next_scene != None:
            current_scene = current_scene.next_scene
    display.__uninit__()

if __name__ == "__main__":
    main()
