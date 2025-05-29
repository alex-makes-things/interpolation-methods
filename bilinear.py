from PIL import Image
import numpy as np
from math import floor

im = Image.open('images/landscape.png')

width, height = im.size
pixels = im.load()
scaling_factor = 2  #can be any integer or decimal even between 0 and 1

new_height = floor(height*scaling_factor)
new_width = floor(width*scaling_factor)

newpixels = []
image_mode = "RGB" if len(pixels[(0,0)]) == 3 else "RGBA"
if image_mode == "RGBA":
    channels = 4
elif image_mode == "RGB":
    channels = 3
else:
    channels = 1

for b in range(new_height):   #move vertically
    for i in range(new_width):    #append horizontally
        scaled_h = b/scaling_factor   #map scaled values to original image grid
        scaled_w = i/scaling_factor
        t_l_pos = (floor(scaled_w), floor(scaled_h))   #top left pixel coordinates
        t_r_pos = (floor(scaled_w), floor(scaled_h)) if (round(scaled_w) == width) else (round(scaled_w), floor(scaled_h))   #top right pixel coordinates, constrained to the original image boundaries
        b_l_pos = (floor(scaled_w), floor(scaled_h)) if (round(scaled_h) == height) else(floor(scaled_w), round(scaled_h))   #bottom left pixel coordinates, constrained to the original image boundaries
        b_r_pos = (floor(scaled_w), floor(scaled_h)) if ((round(scaled_w) == width) or (round(scaled_h) == height)) else (round(scaled_w), round(scaled_h))   #bottom right pixel coordinates, constrained to the original image boundaries

        t_l_pix = pixels[t_l_pos]
        t_r_pix = pixels[t_r_pos]
        b_l_pix = pixels[b_l_pos]
        b_r_pix = pixels[b_r_pos]
        final_pixel = []

        for r in range(channels):
            if (t_l_pos == t_r_pos):
                final_pixel.append(pixels[(t_r_pos)][r])
            elif (b_l_pos == t_l_pos):    #"Division by zero error" fixed
                final_pixel.append(pixels[(b_l_pos)][r])
            else:
                top_lerp = (((t_r_pos[0]-scaled_w)/(t_r_pos[0]-t_l_pos[0]))*t_l_pix[r]) + (((scaled_w-t_l_pos[0])/(t_r_pos[0]-t_l_pos[0]))*t_r_pix[r])
                bottom_lerp = (((t_r_pos[0]-scaled_w)/(t_r_pos[0]-t_l_pos[0]))*b_l_pix[r]) + (((scaled_w-t_l_pos[0])/(t_r_pos[0]-t_l_pos[0]))*b_r_pix[r])
                if top_lerp == bottom_lerp:
                    final_lerp = top_lerp
                else:
                    print((b_l_pos, t_l_pos))
                    final_lerp = (((b_l_pos[1]-scaled_h)/(b_l_pos[1]-t_l_pos[1]))*top_lerp) + (((scaled_h - t_l_pos[1])/(b_l_pos[1]-t_l_pos[1]))*bottom_lerp)
                final_pixel.append(round(final_lerp))

        final_pixel = tuple(final_pixel)
        newpixels.append(final_pixel)

        


newimg = np.array(newpixels, dtype=np.uint8)   #dtype is crucial, data types are very important
newimg= newimg.reshape((new_height,new_width,channels))   #reshape the array into an image
final = Image.fromarray(newimg, mode=image_mode)
final.save("images/scaled.png")
