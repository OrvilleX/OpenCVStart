import numpy as np
import cv2


# 呈现OpenCV默认的读取方式为BGR顺序
def showBGR():
    img = np.zeros((300,300,3), dtype=np.uint8)
    img[:,0:100,0] = 255
    img[:,100:200,1] = 255
    img[:,200:300,2] = 255
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyWindow()


# 针对感兴趣区域ROI的示例
def showROI():
    img = cv2.imread("img/matou.png")
    roi = img[0:300, 0:100, :]
    cv2.imshow("roi", roi)
    override = np.random.randint(0, 255, (300, 100, 3))
    img[0:300, 0:100, :] = override
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyWindow()


def splitWithMerge():
    img = cv2.imread("img/matou.png")
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    cv2.imshow("b", b)
    cv2.imshow("g", g)
    cv2.imshow("r", r)
    b, g, r = cv2.split(img)
    mergeimg = cv2.merge([b, g, r])
    cv2.imshow("mergeimg", mergeimg)
    cv2.waitKey()
    cv2.destroyWindow()


if __name__ == '__main__':
    splitWithMerge()
    # showROI()
    # showBGR()