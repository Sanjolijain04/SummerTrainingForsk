#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

#read an image
image=cv2.imread('index.png')
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

#write an image
cv2.imwrite('my_index.png', image)



#convert the image to gray scale image
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(image)