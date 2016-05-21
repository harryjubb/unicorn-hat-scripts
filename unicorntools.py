import colorsys
import unicornhat

NUM_ROWS = 8
NUM_COLS = 8


def hsv_to_rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)


def hsl_to_rgb(h, s, l):
    return colorsys.hls_to_rgb(h, l, s)


def set_pixel_tuple(x, y, color):
    unicornhat.set_pixel(x, y, color[0], color[1], color[2])
