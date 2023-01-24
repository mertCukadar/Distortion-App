import cv2
import numpy as np
import matplotlib.pyplot as plt
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
            if distance > 12:
                l3.append([l2[i]])
        
        blank_img = np.zeros(np.shape(dst))
        np.shape(blank_img)

        for i in l3:
            print(i[0])
            blank_img[i[0][0],i[0][1]] = 200

        return l3 , blank_img 

    def exact_dot(dst , original_img ,l3):
        blank_dot = np.zeros(np.shape(dst))
        counter = 0
        for i in l3:
            rangex_min = i[0][0] - 20
            rangex_max = i[0][0] + 20
            
            rangey_min = i[0][1] - 20
            rangey_max = i[0][1] + 20
                
            region = original_img[rangex_min : rangex_max , rangey_min : rangey_max]
            
            #local area black and white convertion
            
            region_black_filter = (region > region.mean()) #THİS SECTİON WHİLL BE AOUTOMATİZE WİTH AVARAGE ARRAY "I" VALUE
            region_white_filter = (region < region.mean())
            
            
            region[region_black_filter] = 255
            region[region_white_filter] = 0
            
            
            ##--------------------------------------------------------------
            x_coord = []
            for i in range(40):
            
                #print(f"count of non zero values: {np.mean(np.argwhere(region[i,:] == 0))}")
                x_coord.append(np.mean(np.argwhere(region[i,:] == 0)))
            
                if np.count_nonzero(region[i,:]) < 25:
                    break

            x_index = np.floor(np.mean(x_coord))
            
            
            
            y_coord = []

            for j in range(40):
            
                #print(f"count of non zero values: {np.mean(np.argwhere(region[i,:] == 0))}")
                try:
                    y_coord.append(np.mean(np.argwhere(region[:,j] == 0)))
                except IndexError:
                    continue
                if np.count_nonzero(region[:,j]) < 25:
                    break

            y_index = np.floor(np.mean(y_coord))
            
            ##--------------------------------------------------------------
            if (int == type(x_index)):
                continue
            else:
                try:
                    print(f"x : {x_index} y: {y_index}")
                    #implament blank dot
                    blank_dot[rangex_min : rangex_max , rangey_min : rangey_max][ int(x_index) ,int(y_index)] = 255
                    region[int(y_index) , int(x_index)] = 130
                except ValueError:
                    continue
            
            counter +=1
            # plt.imshow(region)
            # plt.title(counter)
            # plt.show()
            
        return blank_dot 