from PIL import Image
import numpy as np
from math import floor

im = Image.open('minilandscape.png')

width, height = im.size
pixels = im.load()
scaling_factor = 1.5

newpixels = []
for b in range(floor(height*scaling_factor)):
    for i in range(floor(width*scaling_factor)):
        scaled_h = floor(b/scaling_factor)
        scaled_w = floor(i/scaling_factor)
        newpixels.append((pixels[scaled_w, scaled_h][0], pixels[scaled_w, scaled_h][1], pixels[scaled_w, scaled_h][2], pixels[scaled_w, scaled_h][3]))


newimg = np.array(newpixels, dtype=np.uint8)

newimg= newimg.reshape((floor(height*scaling_factor),floor(width*scaling_factor),4))
print(newimg)
final = Image.fromarray(newimg, mode='RGBA')
final.save("scaled.png")
