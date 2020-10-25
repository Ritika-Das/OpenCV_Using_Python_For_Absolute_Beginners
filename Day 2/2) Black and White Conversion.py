import cv2                                                  # importing the cv2 module i.e. computer vision, in python
import numpy as np                                          # importing the numpy module i.e. numerical python, using an alias "np",
                                                            # so that it is easier to type out

import matplotlib.pyplot as plt                             # importing the matplotlib.pyplot module using an alias "plt",
                                                            # for displaying our resultant image in a window

img = cv2.imread('image.png',  cv2.IMREAD_GRAYSCALE)        # getting the original image and converting it to grayscale/Black&White form

cv2.imshow('image', img)                                    # displaying the final image in a new window
cv2.waitKey(0)                                              # waits for delay = 0 milliseconds to handle another event on keypress by user
cv2.destroyAllWindows()                                     # windows necessary to read/open photo are now closed or "destroyed"
