"""
This script will read a file from the current directory and convert it to a black and white image.
Commented lines are kept here for reference.
Running from python interactive terminal gave different results when displaying images.
It seems the command line will opt for 'ImageMagic' for display where the script will choose 
some other wacka-doo plotter for display purposes that does not seem to work very well for 
displaying the same image with any fidelity. 
I belive ImageMagic is required by scipy.misc.imsave.
"""

import numpy as np
import matplotlib.image as mpimg
#from scipy.misc import toimage, imsave
from scipy.misc import imsave
#from matplotlib import pyplot as plt
from PIL import Image

test_data_filename = 'tree.jpg'
#test_data_dir = '/home/bryan/Documents/spikes/'

"""
from PIL import Image
a = Image.open('tree.jpg')
a.show()
"""

"""
The test images are saved as files. Read the images and use them for imput.
"""
# This will read all files in a given directory
# data = np.array([mpimg.imread(name) for name in os.listdir(test_data_dir)], dtype=np.float64)

data = np.array(mpimg.imread(test_data_filename), dtype=np.float64)

# Here we expect data.shape eq to img size in px, e.g. (160, 106, 3)
# TODO: assert
print(data.shape)

"""
Slice-out the black and white picture from color picture
"""
bwimage = data[ :, :, 0]

print(bwimage)

#toimage(bwimage).show()
#plt.imshow(bwimage)
#plt.show()
#Image.fromarray(bwimage)

imsave('bwtree.jpg', bwimage)
