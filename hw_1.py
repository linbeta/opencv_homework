# 作業一：寫一個左右來回跑的正方形
import cv2
import numpy as np
import keyboard

# 製造一個錄影的物件，設定路徑和格式和影格
video_recorder = cv2.VideoWriter("hw_1.mp4", cv2.VideoWriter_fourcc(*"MP4V"), 30, (500, 500))

# 產生一個100 x 100的正方形，設定左上角座標來做移動，右下座標固定各加100即可
# cv2.rectangle(stage, (左上角座標), (右下角座標), (BGR顏色), -1)
# 用x, y 和 r來寫正方形的動作
x = 10
y = 200
r = 0

to_right = True
while True:
    if to_right:
        r += 5
    else:
        r -= 5
    stage = np.full((500, 500, 3), (255, 255, 255), np.uint8)
    # 產生一個100 x 100的正方形
    up_left = (x + r, y)
    down_right = ((x + 100 + r), y + 100)
    rect = cv2.rectangle(stage, up_left, down_right, (0, 0, 0), -1)
    cv2.imshow('Press "q" to quit', rect)

    if x + r > 400:
        to_right = False
    elif x + r < 0:
        to_right = True

    cv2.waitKey(30)
    # 偵測鍵盤，如果按q則跳出
    if keyboard.is_pressed("q"):
        break

    video_recorder.write(rect)


cv2.destroyAllWindows()
video_recorder.release()
