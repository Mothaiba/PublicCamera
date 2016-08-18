import cv2
import numpy as np

if (__name__ == '__main__'):
    Slope_opt = 0.001
    Intersection_opt = 1
    str_path_Bgd = "C:/Users/Champ/Desktop/0002_20160805_075425_03152300.jpg"

    # background image
    img_Bgd = cv2.imread(str_path_Bgd)
    h, w = img_Bgd.shape[:2]
    # verification
    if img_Bgd is None:
        print 'Failed to load the background image!'

    # covert the image to gray scale
    img_Bgd = cv2.cvtColor(img_Bgd, cv2.COLOR_BGR2GRAY)
    # reduce the light changing effect
    cv2.equalizeHist(img_Bgd)

    # Canny
    # img_Bgd = cv2.Canny(img_Bgd, 100, 200)

    # detect objects of interest
    _, contours_Bgd, hierarchy = cv2.findContours(img_Bgd.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    NumBase = contours_Bgd[0][0][0][0]
    trans = np.zeros((h, w, 3), np.uint8)
    cv2.drawContours(trans,contours_Bgd,-1,(0,255,0),3)
    cv2.imshow("contours", img_Bgd)

    0xFF & cv2.waitKey()
    cv2.destroyAllWindows()
