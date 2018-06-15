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
        # cv2.namedWindow('Show Pictures')
        # cv2.imshow('Show Pictures', img)


        # number += 1
    # if cv2.waitKey() == 27 & 0xff == ord("q"):
    #     cv2.destroyAllWindows()
if __name__ == '__main__':
    animation(1)