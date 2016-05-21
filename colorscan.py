import unicorntools
import time

for r in xrange(256):
    for g in xrange(256):
        for b in xrange(256):

            unicorntools.show_all_pixels(r, g, b)
            time.sleep(0.00001)
