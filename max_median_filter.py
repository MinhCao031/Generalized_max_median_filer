from funcs import edge_extend, edge_cut, max_median
from statistics import median
from matplotlib import pyplot as plt
import cv2
import numpy as np
import random

# loading image
img_original = cv2.imread('_img.png')

# converting to gray scale
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# window size
k_size = 5

# filter images
img_long = edge_extend(img_gray, k_size)
img_mmf1 = edge_cut(max_median(img_long,1), k_size)
img_mmf2 = edge_cut(max_median(img_long,2), k_size)
img_mmf4 = edge_cut(max_median(img_long,4), k_size)

# plot images 
# (1,4,x) can be replaced by (2,2,x) depend on image sizes
plt.subplot(1,4,1),plt.imshow(img_gray, cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,4,2),plt.imshow(img_mmf1, cmap = 'gray')
plt.title('mmf k=1'), plt.xticks([]), plt.yticks([])

plt.subplot(1,4,3),plt.imshow(img_mmf2, cmap = 'gray')
plt.title('mmf k=2'), plt.xticks([]), plt.yticks([])

plt.subplot(1,4,4),plt.imshow(img_mmf4, cmap = 'gray')
plt.title('mmf k=4'), plt.xticks([]), plt.yticks([])
 
plt.show()



