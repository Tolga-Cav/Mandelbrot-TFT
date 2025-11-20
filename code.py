import board
import displayio

import mandelbrot


display = board.DISPLAY

MAX_STEPS = 128

bitmap = displayio.Bitmap(display.width, display.height, 2)

color_palette = displayio.Palette(2)
color_palette[0] = 0x000000  # Black
color_palette[1] = 0xFFFFFF  # White


def set_bitmap_value(x, y, steps):
    bitmap[x, y] = 0 if steps == MAX_STEPS else 1


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
