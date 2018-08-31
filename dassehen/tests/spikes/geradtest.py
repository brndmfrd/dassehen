import numpy as np
import matplotlib.image as mpimg
from scipy.misc import imsave
import os

try:
    from dassehen import parallax
except ImportError:
    print('Import failed.')

# Usage as either relative or abs path to img dir.
test_data_dir = '../images/DifImages/'

# Read all files in a given directory
# data is expected to be a (2, n, m) array. If there is a 4th array, the picture may have been in color.
data = np.array([mpimg.imread(test_data_dir + name) for name in os.listdir(test_data_dir)], dtype=np.float64)

stringData = data[0,1495:1500,1495:1500].tolist()
print (*stringData, sep="\n")
print ("\n****************************************\n")
stringData1 = data[1,1495:1500,1495:1500].tolist()
print (*stringData1, sep="\n")

#bwimage0 = data[0,0:600,0:600]
#imsave('bwimage0.jpg', bwimage0)

#bwimage1 = data[1,0:600,0:600]
#imsave('bwimage1.jpg', bwimage1)

bwimage0 = data[0,0:1500,0:1500]
imsave('bwimage0.jpg', bwimage0)

bwimage1 = data[1,0:1500,0:1500]
imsave('bwimage1.jpg', bwimage1)
#parallax.main(data)
