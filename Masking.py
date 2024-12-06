import cv2 as cv
import numpy as np
print("1.Circular_Masking\n2.Rectangular_Masking")
choice=int(input("Enter your choice:"))
path=input("Give your image path:")
img=cv.imread(path)
img=cv.imread('D:\Python\photos&video_opeancv\cats.jpg')
cv.imshow('Original_image',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
if choice==1:
    circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)#masking is applied ar the centere of the image
    masked_1=cv.bitwise_and(img,img,mask=circle)
    cv.imshow('Circular_masking',masked_1)
if choice==2:
    rectangle=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+150,img.shape[0]//2+150),255,-1)
    masked_2=cv.bitwise(img,img,mask=rectangle)
    cv.imshow('Rectangular_masking',masked_2)
cv.waitKey(0)
