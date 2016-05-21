import unicornhat
import unicorntools
import time

print unicorntools.hsl_to_rgb(0.5, 0.5, 0.5)

for y in range(8):
    for x in range(8):
        unicorntools.set_pixel_tuple(x, y, (0, 0, 255))
        unicornhat.show()
        time.sleep(0.05)

time.sleep(1)
