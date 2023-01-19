import matplotlib.pyplot as plt
from Main_Functions.imageFunction import imgFun
import cv2
import numpy as np

img = imgFun.gray_converted_filter()

cv2.imwrite("grayImage.png" , img)

print(np.shape(img))

# plt.imshow(img)
# plt.show()



y = np.array([[0,162],[162,324],[324,486],[486,648],[648,810],[810,972],[972,1134],[1134,1296],[1296,1458],[1458,1620],[1620,1782],[1782,1944],[1944,2106],[2106,2268],[2268,2430],[2430,2592]])
x = np.array([[0,162],[162,324],[324,486],[486,648],[648,810],[810,972],[972,1134],[1134,1296],[1296,1458],[1458,1620],[1620,1782],[1782,1944]])

print(f"x list: {x} \n ------------- \ny list:{y}")

BW_img = imgFun.BW_image(img , x , y)

plt.imshow(BW_img)
plt.show()

dst = imgFun.Harris_corner(BW_img)

plt.imshow(dst)
plt.show()
cv2.imwrite("BW.png" , img)