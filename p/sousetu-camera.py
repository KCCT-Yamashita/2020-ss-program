#起動方法
#python caps.py 0 &
#python caps.py 2 &
#python caps.py 4 &
#ESC で終了
# OpenCVがインストールされている必要がある


import cv2
import sys
args=sys.argv
cap1 = cv2.VideoCapture(int(args[1])) # VideoCaptureのインスタンスを作成する。(複数のカメラがあるときは引数で識別)

while True:
    ret, frame = cap1.read()     # 1フレーム読み込む
    frame = cv2.rotate(frame, cv2.ROTATE_180)   #上下反転
    # 画像を表示する
    cv2.imshow('Image', frame)

    k = cv2.waitKey(1)  #引数は待ち時間(ms)
    if k == 27: #Esc入力時は終了
        break

# 終了処理
cap1.release()
cv2.destroyAllWindows()