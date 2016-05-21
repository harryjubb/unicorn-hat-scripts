import colorsys

def hsv_to_rgb(h, s, v):
  return colorsys.hsv_to_rgb(h, s, v)

def hsl_to_rgb(h, s, l):
  return colorsys.hls_to_rgb(h, l, s)
