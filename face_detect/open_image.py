import cv2

filename = './img/jbs.jpg'


def showPicture():
    img = cv2.imread(filename)
    cv2.namedWindow('Show Pictures')
    cv2.imshow('Show Pictures', img)
    if cv2.waitKey() == 27 & 0xff == ord("q"):
        cv2.destroyAllWindows()


if __name__ == '__main__':
   showPicture()