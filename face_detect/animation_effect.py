# coding=utf-8
import time
import cv2


filename = './img/bmp/8.bmp'
def animation(number):

    filename_temp = './img/bmp/%d.bmp' % number
    print filename_temp
    cv2.destroyAllWindows()
    img = cv2.imread(filename_temp)
    show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return show

if __name__ == '__main__':
    animation(1)