import interface
import scene
from startscene import StartScene

def main():
    display = interface.Interface()
    current_scene = None

    def switch_scene(scene):
        current_scene = scene

    current_scene = StartScene(display)
    ch = ' '
    while ch != 'q':
        ch = display.get_input()
        current_scene.update(display, ch)
        if current_scene.next_scene != None:
            current_scene = current_scene.next_scene
    display.__uninit__()

if __name__ == "__main__":
    main()
