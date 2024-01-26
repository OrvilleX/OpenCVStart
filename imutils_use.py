import numpy as np
import cv2 as cv
import imutils
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 平移图像
def translate():
    img = cv.imread('./img/matou.png')
    translated = imutils.translate(img, 100, 50)
    plt.figure()
    plt.subplot(121)
    plt.imshow(img[:,:,::-1])
    plt.title('原图')
    plt.subplot(122)
    plt.imshow(translated[:,:,::-1])
    plt.title('平移')
    plt.show()


# 缩放图像，会自动根据指定宽或高自动缩放
def resize():
    img = cv.imread('./img/matou.png')
    resize = imutils.resize(img, width=200)
    plt.figure()
    plt.subplot(121)
    plt.imshow(img[:,:,::-1])
    plt.title('原图')
    plt.subplot(122)
    plt.imshow(resize[:,:,::-1])
    plt.title('缩放')
    plt.show()


# 旋转
def rotated():
    img = cv.imread('./img/matou.png')
    rotated = imutils.rotate(img, 90)
    rotated_round = imutils.rotate_bound(img, 90)
    plt.figure()
    plt.subplot(131)
    plt.imshow(img[:,:,::-1])
    plt.title('原图')
    plt.subplot(132)
    plt.imshow(rotated[:,:,::-1])
    plt.title('逆时针')
    plt.subplot(133)
    plt.imshow(rotated_round[:,:,::-1])
    plt.title('正时针')
    plt.show()


# 骨架图
def skeletonize():
    img = cv.imread('./img/matou.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    skeleton = imutils.skeletonize(gray, size=(7, 7))
    plt.figure()
    plt.subplot(131)
    plt.imshow(img[:,:,::-1])
    plt.title('原图')
    plt.subplot(132)
    plt.imshow(skeleton, cmap="gray")
    plt.title('骨架图')
    plt.show()


if __name__ == '__main__':
    img = cv.imread('./img/matou.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    skeleton = imutils.skeletonize(gray, size=(7, 7))
    plt.figure()
    plt.subplot(131)
    plt.imshow(img[:,:,::-1])
    plt.title('原图')
    plt.subplot(132)
    plt.imshow(skeleton, cmap="gray")
    plt.title('骨架图')
    plt.show()