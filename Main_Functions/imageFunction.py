import cv2
import numpy as np
from Files.Files import Files


class imgFun:

    def gray_converted_filter():
        '''
        this function convert the image madian blured and gray scaled. Collected image
        can be configure from Files.py file.
        From '/Files' you can add Images.
        '''
        img = cv2.imread(Files.img)
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        blured_gray = cv2.medianBlur(gray , 1)

        return blured_gray
        
    def thresholer(img):
        avarage = img.mean(axis = (0,1)) - (img.mean(axis = (0,1))/7.5)
        rat , threshold_img = cv2.threshold(img , avarage , 255 , cv2.THRESH_BINARY)
        return threshold_img    

    def GCommonDivisor(img):
        x = []
        y = []
        value = 0
        value2 = 0
        rate = 8

        shape = np.shape(img)

        # set "rate" for sensivity
        gcd = np.gcd(shape[0],shape[1])/rate 

        while value < shape[0]+1:
            x.append(value)
            value += int(gcd)

        while value2 < shape[1]+1:
            y.append(value)
            value2 += int(gcd)

        N = 2
        x = [x[n:n+N] for n in range(0,len(x),N)]
        y = [y[n:n+N] for n in range(0,len(y),N)]

        return x,y

    def BW_image(img,x,y):
        shape = np.shape(img)
        blank_img = np.zeros(shape)
        try:
            for i in range(len(x)):
                for j in range(len(y)):
                    array = img[x[i,0]:x[i,1] , y[j,0] : y[j,1]]
                    blank_img[x[i,0]:x[i,1] , y[j,0] : y[j,1]] = imgFun.thresholer(array)
        except:
            error = "there is a problem"
        return blank_img
        

