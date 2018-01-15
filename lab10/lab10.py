import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('GMIT.jpg',)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imwrite('gray_image.png',gray_image)
#cv2.imshow('color_image',image)
#cv2.imshow('gray_image',gray_image) 
#cv2.waitKey(0)                 # Waits forever for user to press any key
#cv2.destroyAllWindows()        # Closes displayed windows

#7


#blu = cv2.GaussianBlur(gray_image,(13,13),0)


#9,10,11,12

sobelHorizontal = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=5)    # x dir
sobelVertical = cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=5)      # y dir
#absX = cv2.convertScaleAbs(sobelHorizontal)
#absY = cv2.convertScaleAbs(sobelVertical)
sobelsum = sobelHorizontal + sobelVertical;
#blur = cv2.GaussianBlur(image,(3,3),0)
canny = cv2.Canny(image,100,200)


#6 7 8
plt.subplot(2, 3,1),plt.imshow(image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(sobelHorizontal , cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.title('Sobel X')
plt.subplot(2,3,4),plt.imshow(sobelVertical , cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.title('Sobel Y')
plt.subplot(2,3,5),plt.imshow(sobelsum, cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.title('Sobel sum')
plt.subplot(2,3,6),plt.imshow(canny,cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.title('Canny')
plt.show()

#13
img = cv2.imread('minion.jpg')
canny1 = cv2.Canny(img,50,200)

cv2.imshow('Canny-Minion',canny1)
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows

 