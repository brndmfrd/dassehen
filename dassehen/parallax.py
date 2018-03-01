"""
Parallax performs a comparison between two images (read: arrays) and determines depth along a single axis.
Parallax expects a 3-dim array (2, WIDTH, LENGTH); this means two arrays of LENGTH and WIDTH for comparison.

First the images are validated, if they can be compared. 
Each array is mapped to a bit-array where a relative difference in bits indicates a significant change in contrast.
The two bit-arrays are then compared against each other. Where the largest shift in bits are is where we 
determine closer objects to be by the principal of parallax.
"""


import numpy as np


# The number of pixle rows to be evaluated. 
# e.g. '10' indicates 10 above and 10 below the midline, for 21 rows total.
__pixWidth__ = 5


def main(arg):
    """ Entry point for processing parallax with command arguments. """
    # Expect args to be a 3-dim array of (2, LENGTH, WIDTH)
    # TODO: Validate arg shape 
    # TODO: Validate two arrays are same dims
    if arg.shape[0] != 2:
        print('we do not have two arrays to compare')
        return

    img1, img2 = arg
    
    if img1.shape[0] != img2.shape[0]:
        print('arrays are not the same height')
        return

    if img1.shape[1] != img2.shape[1]:
        print('arrays are not the same width')
        return

    if img1.shape[0] < (__pixWidth__ + 2):
        print('picture is not tall enough for this ride')
        return

    midpoint = int(img1.shape[0] / 2)
    topCenter = int(midpoint - __pixWidth__)
    bottomCenter = int(midpoint + __pixWidth__)

    targetRows = img1[topCenter:bottomCenter, :]

    print(targetRows)

