import cv2
import numpy as np

def sobel_filter(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x = np.abs(sobel_x)
    sobel_y = np.abs(sobel_y)
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    sobel_combined = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)


    cv2.imshow('original', gray)
    cv2.imshow('Sobel Filter', sobel_combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return sobel_combined

image_path = 'D:/MyPycharmProjects/Data_science_lesson60_Sobel_Canny_Roberts_Filter/Filarmoniya.jpg'
sobel_filter(image_path)


