# 作業二：把圖片中的文字分離出來
import cv2
import numpy as np

img = cv2.imread("h2.png", 1)

tweak_1 = (2, 2, 51, 0)
tweak_2 = (100, 100, 51, 0)

# 先用除法將顏色變少
result = cv2.divide(img, tweak_1)
# 再做乘法把背景圖片和文字的對比拉大
result = cv2.multiply(result, tweak_2)
# 抽出某個顏色的數值變灰階，y軸和x軸取全部的值，第三個欄位0是B，1是G, 2是R
# 試了一下抽綠色的值效果最好，直接得到答案XD
cv2.imshow("window", result[:, :, 1])

cv2.waitKey(0)
