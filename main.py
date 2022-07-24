import cv2
import numpy as np


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    lena = cv2.imread("img/matou.png")
    # cv2.imshow("lena1", lena)
    # b = lena[:,:,0]
    # g = lena[:,:,1]
    # r = lena[:,:,2]
    # cv2.imshow("b", b)
    # cv2.imshow("g", g)
    # cv2.imshow("r", r)
    # lena[:,:,0] = 0
    # cv2.imshow("lenab0", lena)
    # lena[:,:,1] = 1
    # cv2.imshow("lenab2g0", lena)

    # b, g, r = cv2.split(lena)
    # cv2.imshow("b", b)
    # cv2.imshow("g", g)
    # cv2.imshow("r", r)

    # b, g, r = cv2.split(lena)
    # bgr = cv2.merge([b, g, r])
    # rgb = cv2.merge([r, g, b])
    # cv2.imshow("lena", lena)
    # cv2.imshow("bgr", bgr)
    # cv2.imshow("rgb", rgb)

    # gray = cv2.imread("img/matou.png", 0)
    # print("图像gray属性")
    # print("shape=", gray.shape)
    # print("size=", gray.size)
    # print("dtype=", gray.dtype)
    # print("图像color属性")
    # print("shape=", lena.shape)
    # print("size=", lena.size)
    # print("dtype=", lena.dtype)

    # lenb = lena
    # img1 = np.random.randint(0, 256, size=[3,3], dtype=np.uint8)
    # result1 = lena + lenb  # 取余方式计算像素相加，即和超过255后，取余数
    # result2 = cv2.add(lena, lenb)  # 基于饱和值计算像素相加，即和超过255后取255
    # cv2.imshow("original", lena)
    # cv2.imshow("result1", result1)
    # cv2.imshow("result2", result2)

    # lenb = lena
    # result = cv2.addWeighted(lena, 0.6, lenb, 0.4, 0)  # 加权求和（饱和值），即 图片1x系数1+图片2x系数2+亮度调节量
    # cv2.imshow("origin", lena)
    # cv2.imshow("result", result)

    # b = np.zeros(lena.shape, dtype=np.uint8)
    # b[100:200,100:200,:] = 255
    # result = cv2.bitwise_and(lena, b)
    # cv2.imshow("and", result)

    b = np.zeros(lena.shape, dtype=np.uint8)
    b[100:200, 100:200, :] = 255
    result = cv2.bitwise_or(lena, b)
    cv2.imshow("or", result)

    cv2.waitKey()
    cv2.destroyWindow()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
