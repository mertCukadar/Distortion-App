import matplotlib.pyplot as plt
from Main_Functions.imageFunction import imgFun


img = imgFun.gray_converted_filter()


plt.imshow(img)
plt.show()

x,y = imgFun.GCommonDivisor(img)

print(f"x list: {x} \n ------------- \ny list:{y}")

BW_img = imgFun.BW_image(img , x , y)

plt.imshow(BW_img)
plt.show()
