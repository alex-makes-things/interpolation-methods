from PIL import Image
import numpy as np
from math import floor

im = Image.open('landscape.png')

width, height = im.size
pixels = im.load()
scaling_factor = 1.3  #can be any integer or decimal even between 0 and 1

newpixels = []
try:

    for b in range(floor(height*scaling_factor)):   #move vertically
        for i in range(floor(width*scaling_factor)):    #append horizontally
            scaled_h = floor(b/scaling_factor)    #map scaled values to original image grid
            scaled_w = floor(i/scaling_factor)
            newpixels.append((pixels[scaled_w, scaled_h][0], pixels[scaled_w, scaled_h][1], pixels[scaled_w, scaled_h][2], pixels[scaled_w, scaled_h][3]))
    newimg = np.array(newpixels, dtype=np.uint8)   #dtype is crucial, data types are very important
    newimg= newimg.reshape((floor(height*scaling_factor),floor(width*scaling_factor),4))   #reshape the array into an image
    final = Image.fromarray(newimg, mode='RGBA')

except IndexError:

    print("Image is not RGBA!")
    for b in range(floor(height*scaling_factor)):   #move vertically
        for i in range(floor(width*scaling_factor)):    #append horizontally
            scaled_h = floor(b/scaling_factor)    #map scaled values to original image grid
            scaled_w = floor(i/scaling_factor)
            newpixels.append((pixels[scaled_w, scaled_h][0], pixels[scaled_w, scaled_h][1], pixels[scaled_w, scaled_h][2]))
    newimg = np.array(newpixels, dtype=np.uint8)
    newimg= newimg.reshape((floor(height*scaling_factor),floor(width*scaling_factor),3))
    final = Image.fromarray(newimg, mode='RGB')


final.save("scaled.png")
