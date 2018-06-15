# coding=utf-8
import os
import shutil
import time

import cv2


def faceDetect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    camera = cv2.VideoCapture()
    while (True):
        try:
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('VideoFaceDetect', frame)
            k = cv2.waitKey(1)
            if k == ord("q"):
                    break
        except Exception as e:
            print e
            break
    camera.release()
    cv2.destroyAllWindows()

from open_image import filename
def facd_detect():
    face_cascade = cv2.CascadeClassifier('./res/haarcascade_frontalface_alt.xml')
    img = cv2.imread(filename)

    count = 1
    try:
        faces = face_cascade.detectMultiScale(img, 1.1, 5)
        print faces
        if len(faces):
            for (x, y, w, h) in faces:
                while(1):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.imshow('VideoFaceDetect', img)
                    k = cv2.waitKey(1)
                    if k == ord("q"):
                        break

                # if w >= 128 and h >= 128:
                # # 以时间戳和读取的排序作为文件名称
                #     listStr = [str(int(time.time())), str(count)]
                #     fileName = ''.join(listStr)
                #     # 扩大图片，可根据坐标调整
                #     X = int(x * 0.5)
                #     W = min(int((x + w) * 1.2), img.shape[1])
                #     Y = int(y * 0.3)
                #     H = min(int((y + h) * 1.4), img.shape[0])
                #
                #     f = cv2.resize(img[Y:H, X:W], (W - X, H - Y))
                #     cv2.imwrite('img' + os.sep + '%s.jpg' % fileName, f)
                #     count += 1
                #     print  './' + "have face"
    except Exception as e:
        print e
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # faceDetect()
    facd_detect()