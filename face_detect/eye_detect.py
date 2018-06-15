# coding=utf-8
# detecMultiScale()函数
# 参数1：image--待检测图片，一般为灰度图像加快检测速度；
# 参数2：objects--被检测物体的矩形框向量组；
# 参数3：scaleFactor--表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
# 参数4：minNeighbors--表示构成检测目标的相邻矩形的最小个数(默认为3个)。
#         如果组成检测目标的小矩形的个数和小于 min_neighbors - 1 都会被排除。
#         如果min_neighbors 为 0, 则函数不做任何操作就返回所有的被检候选矩形框，
#         这种设定值一般用在用户自定义对检测结果的组合程序上；
# 参数5：flags--要么使用默认值，要么使用CV_HAAR_DO_CANNY_PRUNING，如果设置为
#         CV_HAAR_DO_CANNY_PRUNING，那么函数将会使用Canny边缘检测来排除边缘过多或过少的区域，
#         因此这些区域通常不会是人脸所在区域；
# 参数6、7：minSize和maxSize用来限制得到的目标区域的范围。

import cv2


def eyeDetect():
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5, 0, (40, 40))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        cv2.imshow('VideoFaceDetect', frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
                break
    camera.release()
    cv2.destroyAllWindows()
from open_image import filename
def eydDetect():
    eye_cascade = cv2.CascadeClassifier('./img/haarcascade_eye.xml')
    img = cv2.imread(filename)
    print eye_cascade.detectMultiScale(img, 1.2, 5, 0, (40, 40))
    while (True):

        eyes = eye_cascade.detectMultiScale(img, 1.2, 5, 0, (40, 40))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        cv2.imshow('VideoFaceDetect', img)
        k = cv2.waitKey(1)
        if k == ord("q"):
                break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # eyeDetect()
    eydDetect()