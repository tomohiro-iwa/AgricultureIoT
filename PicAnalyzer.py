import cv2
import numpy as np

RED = 2
GREEN = 1
BLUE = 0

def imshow(label,mat):
  cv2.imshow(label, mat)
  cv2.waitKey()
  cv2.destroyAllWindows()

img = cv2.imread('./test.png')

## 緑だけを抽出した例 しきい値 125以上の場合だけ黒にした画像
_, ret = cv2.threshold(img[:,:, GREEN], 125, 255, cv2.THRESH_BINARY)
imshow("緑色がしきい値以上の部分", ret)
_, ret = cv2.threshold(img[:,:, BLUE], 125, 255, cv2.THRESH_BINARY)
imshow("blue色がしきい値以上の部分", ret)
_, ret = cv2.threshold(img[:,:, RED], 125, 255, cv2.THRESH_BINARY)
imshow("red色がしきい値以上の部分", ret)

redimg = img[:,:, RED]
greenimg = img[:,:, GREEN]
blueimg = img[:,:, BLUE]

#imshow("red", redimg)
#imshow("green", greenimg)
#imshow("blue", blueimg)

other =  (blueimg + redimg) /2
result = greenimg - other
#imshow("緑から青と赤の平均を引いた画像", result)
#imshow("緑から青を引いた画像", greenimg - blueimg)
#imshow("緑から赤を引いた画像", greenimg - redimg)



