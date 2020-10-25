# Subtraction Operation on two images - or Negative Second Image Added Onto First Image

import cv2                                    # importing the cv2 module i.e. computer vision, in python
import numpy as np                            # importing the numpy module i.e. numerical python, using an alias "np",
                                              # so that it is easier to type out

image1 = cv2.imread('image.png')              # getting the original image1 loaded with image.png
image2 = cv2.imread('umage.png')              # getting the original image2 loaded with umage.png

sub = cv2.subtract(image1, image2)            # we subtract image2's pixels from that of image1's pixels
                                              # or simply, we produce the negative of image2,
                                              # and add the same with image1

cv2.imshow('Subtracted Image', sub)           # displaying the final image in a new window with 'Subtracted Image' as Title bar
  
if cv2.waitKey(0) & 0xff == 27:               # Memory is freed or "de-allocated"
    cv2.destroyAllWindows()                   # where delay = 0, so zero wait for user's keypress
