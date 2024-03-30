import cv2
import numpy as np

image = cv2.imread("/home/tanmay/Documents/code/ML/notesorganizer/buffer/red.jpeg")

#declerations


cv2.imshow("Input Buffer Image", image)
    
b = image[:, :, :1]
g = image[:, :, 1:2]
r = image[:, :, 2:]

b_mean = np.mean(b)
g_mean = np.mean(g)
r_mean = np.mean(r)
  

if (b_mean > g_mean and b_mean > r_mean):
    print("Blue")
    result = "Blue"
if (g_mean > r_mean and g_mean > b_mean):
    print("Green")
    result = "Green"
else:
    print("Red")
    result = "Red"

