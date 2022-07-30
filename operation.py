import numpy as np
import cv2


def imgAdd():
    img1 = cv2.imread("img/matou.png")
    img2 = cv2.imread("img/matou.png")
    imgAdd = img1 + img2
    cv2.imshow("add", imgAdd)
    imgCVAdd = cv2.add(img1, img2)
    cv2.imshow("cvadd", imgCVAdd)
    imgWeighted = cv2.addWeighted(img1, 0.5, img2, 1, 0)
    cv2.imshow("addWeighteds", imgWeighted)
    cv2.waitKey()
    cv2.destroyWindow()


if __name__ == '__main__':
    imgAdd()