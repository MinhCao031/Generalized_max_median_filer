from funcs import edge_extend, edge_cut, max_median, general_max_median
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
k_size = 2

# filter
img_long = edge_extend(img_gray, k_size)
img_blur = edge_cut(max_median(img_long,k_size), k_size)
img_blur1 = edge_cut(general_max_median(img_long,k_size,1), k_size)
img_blur2 = edge_cut(general_max_median(img_long,k_size,2), k_size)

# plot images
# (2,2,x) can be replaced by (1,4,x) depend on image sizes
plt.subplot(2,2,1),plt.imshow(img_gray, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(img_blur, cmap = 'gray')
plt.title('MMF k = 2'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(img_blur1, cmap = 'gray')
plt.title('general r=1'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(img_blur2, cmap = 'gray')
plt.title('general r=2'), plt.xticks([]), plt.yticks([])

plt.show()