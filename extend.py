import cv2
import numpy as np
from matplotlib import pyplot as plt
from funcs import edge_extend, edge_cut

# loading image
img_original = cv2.imread('_img2extend.png')

# converting to gray scale
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# extend images
img = edge_extend(img_gray,100)

# plot images
plt.subplot(1,2,1),plt.imshow(img_gray, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2),plt.imshow(img, cmap = 'gray')
plt.title('Extend Pixels'), plt.xticks([]), plt.yticks([])

plt.show()