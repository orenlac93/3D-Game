from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController


app = Ursina()

window.title = 'Minecraft Lite \U0001F600'         # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Full screen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

Sky(texture='sky')
player = FirstPersonController()

boxes = []
for i in range(25):
    for j in range(25):
        box = Button(color=color.white,
                     model='cube',
                     position=(j, 0, i),
                     texture='grass',
                     parent=scene,
                     highlight_color=color.lime,
                     origin_y=0.5)
        boxes.append(box)

hand = Entity(
    model='cube',
    scale=(0.2, 0.2),
    color=color.orange,
    rotation=Vec3(150, -10, 0),
    position=Vec2(0.4, -0.4),
    parent=camera.ui,

)


def update():
    if held_keys['left mouse']:
        hand.position = (0.4, -0.5)
    elif held_keys['right mouse']:
        hand.position = (0.4, -0.5)
    else:
        hand.position = (0.5, -0.6)


def input(key):

    if key == 'q':
        quit()

    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=color.dark_gray,
                    model='cube',
                    position=box.position + mouse.normal,
                    parent=scene,
                    highlight_color=color.lime,
                    origin_y=0.5)

                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)


app.run()

