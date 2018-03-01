"""
This script will read a file from the current directory and convert it to a black and white image.
"""

import numpy as np
import matplotlib.image as mpimg
from scipy.misc import imsave

test_data_filename = 'tree.jpg'

# The test images are saved as files. Read the images and use them for imput.
data = np.array(mpimg.imread(test_data_filename), dtype=np.float64)

#Slice-out the black and white picture from color picture
bwimage = data[ :, :, 0]

# Save array as image to disc
imsave('bwtree.jpg', bwimage)
