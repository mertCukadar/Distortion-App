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
            y.append(value2)
            value2 += int(gcd)

        N = 2
        x = [x[n:n+N] for n in range(0,len(x),N)]
        y = [y[n:n+N] for n in range(0,len(y),N)]

        return x,y

    def BW_image(img,x,y):
        shape = np.shape(img)
        blank_img = np.zeros(shape)
        for i in range(len(x)):
            for j in range(len(y)):
                array = img[x[i][0] : x[i][1] , y[j][0] : y[j][1]]
                blank_img[x[i][0] : x[i][1] , y[j][0] : y[j][1]] = imgFun.thresholer(array)
        return blank_img
        

    def Harris_corner(BW):
        blankimg = np.zeros(np.shape(BW))
        img = np.float32(BW)
        dst = cv2.cornerHarris(img,4,7,0.07)
        dst = cv2.dilate(dst,None)
        blankimg[dst>0.03*dst.max()] = 255
        return  blankimg

    def filter_local(dst):
        shape = np.shape(dst)
        l1 = [] #filter black parts of image
        l2 = []
        index = 1


        for i in range(shape[0]):
             for j in range(shape[1]):
                control = (dst[i,j] > 200)
                if control == True:
                   l1.append([i,j])

        for i in l1:
      
            if  index == len(l1):
                break
    
    
            distance = np.sqrt((i[0] - l1[index][0])**2 + (i[1] - l1[index][1])**2)
            index += 1 
            #print(distance)
            if distance > 30:
                l2.append(i)
            else:
                continue
  
        l3 = []
        l3.append([l2[0]])
        for i in range(len(l2)):
            distance = l2[i][0] -l3[-1][0][0] 
            if distance == 0: 
                l3.append([l2[i]])
            if distance > 10:
                l3.append([l2[i]])
        
        blank_img = np.zeros(np.shape(dst))
        np.shape(blank_img)

        for i in l3:
            print(i[0])
            blank_img[i[0][0],i[0][1]] = 200

        return l3 , blank_img 

