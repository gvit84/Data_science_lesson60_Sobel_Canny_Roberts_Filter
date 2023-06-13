import cv2
import numpy as np

def canny_filter(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    cv2.imshow('original', gray)
    cv2.imshow('Canny Filter', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = 'D:/MyPycharmProjects/Data_science_lesson60_Sobel_Canny_Roberts_Filter/Filarmoniya.jpg'
canny_filter(image_path)