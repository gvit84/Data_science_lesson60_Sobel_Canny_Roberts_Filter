import cv2
import numpy as np

def roberts_filter(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    roberts_x = np.array([[1, 0], [0, -1]])
    roberts_y = np.array([[0, 1], [-1, 0]])

    filtered_x = cv2.filter2D(gray, -1, roberts_x)
    filtered_y = cv2.filter2D(gray, -1, roberts_y)

    gradient = np.sqrt(np.square(filtered_x) + np.square(filtered_y))
    gradient = np.uint8(gradient)

    cv2.imshow("Original", gray)
    cv2.imshow("Roberts Filter Result", gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'D:/MyPycharmProjects/Data_science_lesson60_Sobel_Canny_Roberts_Filter/Filarmoniya.jpg'
roberts_filter(image_path)



