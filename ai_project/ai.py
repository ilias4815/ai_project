import cv2
import numpy as np
# первый урок
# img = cv2.imread(r"C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\image.png")
# img = cv2.resize(img,(1280,800))
# img = cv2.GaussianBlur(img, (3,3),)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img = cv2.Canny(img, 100, 100)
# kernel = np.ones((1, 1), np.uint8)
# img = cv2.dilate(img, kernel, iterations=1)

# img = cv2.erode(img, kernel, iterations=1)

# cv2.imshow("Result", img)
# print(img.shape)

# cv2.waitKey(0)


# cap = cv2.VideoCapture(0)
# cap.set(9, 1000)
# cap.set(9, 1000)


# while True:
#     new, img = cap.read()
#     cv2.imshow("Pizdec", img)

#     if cv2.waitKey(5) & 0xFF == ord("q"):
#         break







# # второй урок
# photo = np.zeros((500, 500, 3), dtype="uint8")
# photo[250:300, 250:300] = 235, 52, 134
# cv2.rectangle(photo, (0,0), (100,100),(235, 52, 134), thickness=cv2.FILLED)
# cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1],photo.shape[0] // 2), (235,52,134), thickness=3)
# cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (235, 52, 134), thickness=3)
# cv2.putText(photo, " ETO PIZDEC", (150, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), thickness=3)


# cv2.imshow("NAVI", photo)
# cv2.waitKey(0)





# третий урок

img = cv2.imread(r"C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\image.png")
new_img = np.zeros(img.shape, dtype="uint8")
# cap = cv2.VideoCapture(r"C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\cv2\ai_project\videos\123.MOV")
# img = cv2.flip(img, -1)
# def rotate(img_param, angle):
    # height, width = img_param.shape[:2]
    # point = (width//2, height//2)

    # mat = cv2.getRotationMatrix2D(point, angle, 2)
    # return cv2.warpAffine(img_param, mat, (width, height))
# img = rotate(img, 270)    
# def tranform(img_param, x, y):
    # mat = np.float32([[1, 0, x], [0, 1, y]])
    # return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))
# img = tranform(img,  30, 100)    
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE, )

cv2.drawContours(new_img, con, -1, (233, 175, 123), 1)


cv2.imshow("Resilt", new_img)
cv2.waitKey(0)