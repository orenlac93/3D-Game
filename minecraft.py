from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController

import player
import map

# init ursina engine
app = Ursina()

window.title = 'Minecraft Lite \U0001F600'         # The window title
window.borderless = False                          # Show a border
window.fullscreen = False                          # Do not go Full screen
window.exit_button.visible = False                 # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True                  # Show the FPS (Frames per second) counter

# init the map view
Sky(texture='sky')

# first person player view
FirstPersonController()

# map object
game_map = map.Map()
game_map.init_boxes()

current_color = color.white


# player object
player = player.Player()
player.init_hand()


def update():
    global current_color

    if held_keys['left mouse']:
        player.hand.position = (0.4, -0.5)
    elif held_keys['right mouse']:
        player.hand.position = (0.4, -0.5)
    else:
        player.hand.position = (0.5, -0.6)

    if held_keys['1']:
        current_color = map.gray
    if held_keys['2']:
        current_color = map.green
    if held_keys['3']:
        current_color = map.brown



def input(key):

    if key == 'q':
        quit()

    for box in game_map.boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=current_color,
                    model='cube',
                    texture='grass',
                    position=box.position + mouse.normal,
                    parent=scene,
                    highlight_color=color.lime,
                    origin_y=0.5)

                game_map.boxes.append(new)
            if key == 'right mouse down':
                game_map.boxes.remove(box)
                destroy(box)


app.run()

