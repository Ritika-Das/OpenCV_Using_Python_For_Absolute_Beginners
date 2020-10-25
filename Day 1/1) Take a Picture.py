import cv2                                          # importing the cv2 module i.e. computer vision, in python

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)         # here our camera_port variable is 0, 
                                                    # since we are shooting the photo afresh from our webcam instead of a saved photo
return_value, image = camera.read()                 # asking the webcam to "read" or click our photo
cv2.imwrite("image.png", image)                     # saving or "writing" our clicked photo as a new file called "image.png"
camera.release()                                    # webcam is signalled to release the handle and turn itself off
cv2.destroyAllWindows()                             # windows necessary to click photo are now closed or "destroyed"
