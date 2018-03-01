import numpy as np
import matplotlib.image as mpimg
from scipy.misc import imsave
import os

try:
    from dassehen import parallax
except ImportError:
    print('Import failed.')

# Usage as either relative or abs path to img dir.
test_data_dir = './images/'

# Read all files in a given directory
# data is expected to be a (2, n, m) array. If there is a 4th array, the picture may have been in color.
data = np.array([mpimg.imread(test_data_dir + name) for name in os.listdir(test_data_dir)], dtype=np.float64)

parallax.main(data)
