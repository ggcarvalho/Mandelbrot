from complex import *
from PIL import Image, ImageDraw
MAX_ITER = 80

def mandelbrot(c:Complex):
    z = Complex(0, 0)
    n = 0
    while z.norm() <= 2 and n < MAX_ITER:
        z = z.times(z)
        z = z.add(c)
        n += 1
    return n

width = 600
height = 400



x0 = -2
x1 = 1
y0 = -1
y1 = 1

palette = []

im = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, width):
    for y in range(0, height):
        c = Complex(x0 + (x / width) * (x1 - x0), y0 + (y / height) * (y1 - y0))
        m = mandelbrot(c)
        color = 255 - int(m * 255 / MAX_ITER)
        draw.point([x, y], (color, color, color))
im.save('Mandelbrot.png', 'PNG')