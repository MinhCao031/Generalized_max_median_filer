from statistics import median
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

# img: input images
# size: amount of pixels to extend
def edge_extend(img, size):
    m = img.shape[0] + 2*size
    n = img.shape[1] + 2*size
    ans = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            I = 0 if i < size else (m-2*size-1 if i+size >= m else i-size)
            J = 0 if j < size else (n-2*size-1 if j+size >= n else j-size)
            ans[i][j] = img[I][J]    
    return np.array(ans)

# img: input images
# size: amount of pixels to cut (usually cut from extended imaged)
def edge_cut(img, size):
    m = img.shape[0]
    n = img.shape[1]
    return np.array(img[size:m-size, size:n-size])

# img: input images
# 2*k+1 = window size 
def max_median(img,k):
    m = img.shape[0]
    n = img.shape[1]
    ans = img
    for i in range(k, m-k):
        for j in range(k, n-k):
            w1 = img[i,j-k:j+k+1]
            w2 = [img[i-x][j+x] for x in range(-k,k+1)]
            w3 = img[i-k:i+k+1,j]
            w4 = [img[i-x][j+x] for x in range(-k,k+1)]
            z = [median(w1), median(w2), median(w3), median(w4)]
            ans[i][j] = int(max(z))
    return np.array(ans)

# img: input images
# 2*k+1 = window size 
# r can vary from 1 to k
def general_max_median(img,k,r):
    m = img.shape[0]
    n = img.shape[1]
    temp_arr = np.array(range(-k,k+1))
    temp_arr = np.delete(temp_arr, k)
    ans = img
    rdm = 0
    for i in range(k, m-k):
        for j in range(k, n-k):
            w1 = np.sort([img[i][j+x] for x in temp_arr])
            w2 = np.sort([img[i+x][j+x] for x in temp_arr])
            w3 = np.sort([img[i+x][j] for x in temp_arr])
            w4 = np.sort([img[i-x][j+x] for x in temp_arr])
            
            sm_arr1 = [w1[r-1], w2[r-1], w3[r-1], w4[r-1]]
            sm_arr2 = [w1[2*k-r], w2[2*k-r], w3[2*k-r], w4[2*k-r]]
            S1 = max(sm_arr1)
            S2 = max(sm_arr2)
            
            if r==k and random.randint(1,100) == 1 and rdm > 0:
                print("\n\n\n",i,j)
                print(w1,w2,w3,w4)
                print(sm_arr1,sm_arr2)
                print(S1,S2)
                rdm -= 1
            
            ans[i][j] = int(median([img[i][j],S1,S2]))
    return ans