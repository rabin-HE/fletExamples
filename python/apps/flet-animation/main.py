import random
from math import pi

import flet
from flet import Container, ElevatedButton, Page, Stack, colors


def main(page: Page):

    size = 40
    gap = 6
    duration = 2000

    c1 = Colors.PINK_500
    c2 = Colors.AMBER_500
    c3 = Colors.LIGHT_GREEN_500
    c4 = Colors.DEEP_PURPLE_500

    all_colors = [
        Colors.AMBER_400,
        Colors.AMBER_ACCENT_400,
        Colors.BLUE_400,
        Colors.BROWN_400,
        Colors.CYAN_700,
        Colors.DEEP_ORANGE_500,
        Colors.CYAN_500,
        Colors.INDIGO_600,
        Colors.ORANGE_ACCENT_100,
        Colors.PINK,
        Colors.RED_600,
        Colors.GREEN_400,
        Colors.GREEN_ACCENT_200,
        Colors.TEAL_ACCENT_200,
        Colors.LIGHT_BLUE_500,
    ]

    parts = [
        # F
        (0, 0, c1),
        (0, 1, c1),
        (0, 2, c1),
        (0, 3, c1),
        (0, 4, c1),
        (1, 0, c1),
        (1, 2, c1),
        (2, 0, c1),
        # L
        (4, 0, c2),
        (4, 1, c2),
        (4, 2, c2),
        (4, 3, c2),
        (4, 4, c2),
        (5, 4, c2),
        (6, 4, c2),
        # E
        (8, 0, c3),
        (9, 0, c3),
        (10, 0, c3),
        (8, 1, c3),
        (8, 2, c3),
        (9, 2, c3),
        (10, 2, c3),
        (8, 3, c3),
        (8, 4, c3),
        (9, 4, c3),
        (10, 4, c3),
        # T
        (12, 0, c4),
        (13, 0, c4),
        (14, 0, c4),
        (13, 1, c4),
        (13, 2, c4),
        (13, 3, c4),
        (13, 4, c4),
    ]

    width = 16 * (size + gap)
    height = 5 * (size + gap)

    canvas = Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    # spread parts randomly
    for i in range(len(parts)):
        canvas.controls.append(
            Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    def randomize(e):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.3
        go_button.visible = True
        again_button.visible = False
        page.update()

    def assemble(e):
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = top * (size + gap)
            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1
        go_button.visible = False
        again_button.visible = True
        page.update()

    go_button = ElevatedButton("Go!", on_click=assemble)
    again_button = ElevatedButton("Again!", on_click=randomize)

    randomize(None)

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.spacing = 30
    page.add(canvas, go_button, again_button)


flet.app(main)
