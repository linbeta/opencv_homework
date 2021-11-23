# 作業三：對影片中的筆拉框標記它
import cv2
import numpy as np
# 讀取影片
video_frames = cv2.VideoCapture("h3.mp4")
video_is_open = video_frames.isOpened()
print("每秒影格數(FPS)", video_frames.get(5))
while video_is_open:
    play, frame = video_frames.read()
    if play:
        # 轉成灰階
        gray_pic = frame[:, :, 2]
        # 做乘法將背景顏色弄淺一點
        mask = cv2.multiply(gray_pic, 2)

        # 取出顏色較深的區塊，讓取出的區塊膨脹，比較容易框出筆的輪廓
        mask = cv2.inRange(mask, 20, 120)
        # mask = cv2.bitwise_not(mask)
        mask = cv2.dilate(mask, np.ones((10, 10)))
        # cv2.imshow("test", mask)

        # 抓出輪廓
        con_num, con_data = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # print("輪廓數量：", len(con_num))

        # 用biggest來存當有多個輪廓時，虛擬外框最大的那個，rectangle來存框出來的長方形面積
        biggest = 1
        rectangle = 0
        # 影片每張frame框出的輪廓數量不一樣，用一個for迴圈來找出最大的輪廓
        for i in range(len(con_num)):
            (x, y, w, h) = cv2.boundingRect(con_num[i])
            if w * h > rectangle:
                rectangle = w * h
                biggest = i
        # 用try / except來處理影片中有幾個frame沒有讀到輪廓的狀況
        try:
            # 繪製輪廓：用紅色，粗細2的線把輪廓畫出來
            # cv2.drawContours(frame, con_num, 1, (0, 0, 255), 2)
            # 標示出虛擬外框，用紅色正方形框出來
            (x, y, w, h) = cv2.boundingRect(con_num[biggest])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow("video", frame)
        except:
            cv2.imshow("video", frame)

        # 影片為30 fps 抓個接近的值讓影片播放速度接近原始檔：1000ms / 30 = 33.33333
        cv2.waitKey(33)
    else:
        break

