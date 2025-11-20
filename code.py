import board
import displayio
import time

import mandelbrot
import color_map


display = board.DISPLAY

MAX_STEPS = 128
PALETTE_SIZE = 2

bitmap = displayio.Bitmap(display.width, display.height, PALETTE_SIZE)

color_palette = displayio.Palette(PALETTE_SIZE)
color_palette[0] = 0x000000  # Black
color_palette[1] = 0xFFFFFF  # White


def set_bitmap_value(x, y, steps):
    bitmap[x, y] = color_map.get_color_map_value(steps, MAX_STEPS, len(color_palette))


# TODO - the generate_matrix function takes a long time to run. We could look at how to optimize it (although the conclusion might be to use C instead...)

mandelbrot.generate_matrix(
    xmin=-2.0,
    xmax=1.0,
    width=display.width,
    ymin=-1.5,
    ymax=1.5,
    height=display.height,
    max_steps=MAX_STEPS,
    set_value=set_bitmap_value,
)


group = displayio.Group()
tile_grid = displayio.TileGrid(bitmap, pixel_shader=color_palette)
group.append(tile_grid)
display.root_group = group

while True:
    pass
