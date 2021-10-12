from ursina import *

gray = color.dark_gray
green = color.white
brown = color.brown


class Map:

    boxes = []

    def init_boxes(self):

        for i in range(25):
            for j in range(25):
                box = Button(color=color.white,
                             model='cube',
                             position=(j, 0, i),
                             texture='grass',
                             parent=scene,
                             highlight_color=color.lime,
                             origin_y=0.5)
                self.boxes.append(box)