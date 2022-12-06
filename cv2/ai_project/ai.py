import cv2

img = cv2.imread('picture/image.jpg')
cv2.imshow('Result NAVI', img)

cv2.waitKey(0)