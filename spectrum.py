import unicorntools
import time

NUM_COLORS = 100000
WAIT_TIME = 0.001

hue = 0

while 1:

    if hue >= NUM_COLORS:
        hue = 0

    hue_float = hue / float(NUM_COLORS)

    color = unicorntools.hsl_to_rgb(
        hue_float,
        1.0,
        0.5
    )

    color_256 = tuple([int(round(x*255)) for x in color])
    # print hue, hue_float, color, color_256

    unicorntools.show_all_pixels(*color_256, brightness=1)

    if WAIT_TIME:
        time.sleep(WAIT_TIME)

    hue += 1
