import sys
import cv2
import numpy as np

def imshow(label,mat):
  cv2.imshow(label, mat)
  cv2.waitKey()
  cv2.destroyAllWindows()

img = cv2.imread(sys.argv[1])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 緑色のHSVの値域1
hsv_min = np.array([30, 30, 0])
hsv_max = np.array([90,255,255])

# 緑色領域のマスク（255：赤色、0：赤色以外）    
mask = cv2.inRange(hsv, hsv_min, hsv_max)

# 白黒画像の表示
#imshow("mask", mask)

# 緑だけ抜き出した画像の表示
masked_img = cv2.bitwise_and(img, img, mask=mask)

imshow("hsv", masked_img)
print(np.sum(mask)/255)
