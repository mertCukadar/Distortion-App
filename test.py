x = [[0, 81], [162, 243], [324, 405], [486, 567], [648, 729], [810, 891], [972, 1053], [1134, 1215], [1296, 1377], [1458, 1539], [1620, 1701], [1782, 1863], [1944]]
y = [[0, 81], [162, 243], [324, 405], [486, 567], [648, 729], [810, 891], [972, 1053], [1134, 1215], [1296, 1377], [1458, 1539], [1620, 1701], [1782, 1863], [1944, 2025], [2106, 2187], [2268, 2349], [2430, 2511], [2592]]


import numpy as np
from Main_Functions.imageFunction import imgFun
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("grayImage.png")

# def BW_image(img,x,y):
#     shape = np.shape(img)
#     blank_img = np.zeros(shape)
#     for i in range(len(x)):
#         for j in range(len(y)):
#             array = img[x[i , 0] : x[i , 1] , y[j , 0] : y[j , 1]]
#             blank_img[x[i , 0] : x[i , 1] , y[j , 0] : y[j , 1]] = imgFun.thresholer(array)
#     return blank_img
        

# BWimg = BW_image(img , x, y)
# plt.imshow(BWimg)
# plt.show()


print(x[0][0])