from ursina import *


class Player:

    hand = None

    def init_hand(self):

        self.hand = Entity(
            model='cube',
            scale=(0.2, 0.2),
            color=color.orange,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.4),
            parent=camera.ui
        )

