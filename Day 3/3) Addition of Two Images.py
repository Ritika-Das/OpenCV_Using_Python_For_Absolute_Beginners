# Arithmetic Operation on two images - or Double Exposure image generation using Weightage

import cv2                                                      # importing the cv2 module i.e. computer vision, in python
import numpy as np                                              # importing the numpy module i.e. numerical python, using an alias "np",
                                                                # so that it is easier to type out

image1 = cv2.imread('image1.png')                               # getting the original image1 loaded
image2 = cv2.imread('image2.png')                               # getting the original image2 loaded

weightedSum = cv2.addWeighted(image1, 0.5, image2, 2.7, 0)      # the second parameter 0.5 and the fourth parameter 2.7 can be increased/decreased
                                                                # to increase/decrease weightage of that particular image in the resultant image
                                                                # Suggestion - try with 0.3 and 0.5, instead of 0.5 and 2.7, and compare the results

cv2.imshow('Weighted Image', weightedSum)                       # displaying the final image in a new window with 'Weighted Image' as Title bar
   
if cv2.waitKey(0) & 0xff == 27:                                 # Memory is freed or "de-allocated"
    cv2.destroyAllWindows()                                     # where delay = 0, so zero wait for user's keypress
