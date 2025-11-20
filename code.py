import board
import displayio

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

# TODO - in order to make the image look better, we should make the aspect ratio correct.
# This can be done by looking at the display width/height ratio and adjusting the xmin/xmax or ymin/ymax ranges accordingly.

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
    # TODO - instead of just generating and displaying a static image, we want to have interactivity.
    # Our current plan for this is:
    # - There are three different actions we need: moving vertically, moving horizontally, and zooming in/out
    # - Since the board has three buttons, our idea is to have holding each button to represent one of these actions,
    #     and then the other two buttons are for either increasing or decreasing the respective value.
    # - For example, naming the buttons A, B and C, holding A and pressing B might move left, while holding A and pressing C might move right.
    # - Doing this, though, will require re-computing the image (although we can optimize a bit by re-using current parts), and currently the image
    #     generation is slow, so we may need to optimize that first.
    pass
