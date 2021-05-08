#!/usr/bin/env python3

import numpy as np
import imageio
import sys


def getBPS(img1, bits):

    return (bits/(img1.shape[0]*img1.shape[1]))
   


# load images
image1 = imageio.imread(sys.argv[1])
bits = sys.argv[2]

bits = int(float(bits))

image1 = image1.astype(dtype=np.uint64)

getBPS(image1, bits)



print("The BPS of the ", sys.argv[1], " compression is:", getBPS(image1, bits))

# return getMSE(image1, image2)
