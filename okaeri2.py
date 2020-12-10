# ライブラリのインポート      ++++++++++++++++++++++++++++++++++++++++
#Q→子機　巻取り
#Z→子機　吐き出す
#W→オムニ左旋回
#X→オムニ右旋回
#E→ハの字にする
#C→||の字にする
#矢印キー→動く


import RPi.GPIO as GPIO
import time
from pygame.locals import *
import pygame
import sys

pygame.init()# Pygameを初期化
screen = pygame.display.set_mode((400, 330))# 画面を作成
pygame.display.set_caption("keyboard event")# タイトルを作成

# モータードライバーを接続したGPIOピンの定義(1:GPIO 2:GPIO 3:GND)
pin11, pin12, pin13 = 29, 31, 30
pin21, pin22, pin23 = 8, 10, 9
pin31, pin32, pin33 = 38, 40, 39
pin41, pin42, pin43 = 19, 21, 20 
pin51, pin52, pin53 = 24, 26, 25

# いろんな変数の定義
Input1, Input2, Input3, Input4, Input5 = 0, 0, 0, 0, 0
V1, V2, V3, V4, V5 = 0, 0, 0, 0, 0
Record1, Record2, Record3, Record4, Record5 = 0, 0, 0, 0, 0
Phase1, Phase2, Phase3, Phase4, Phase5 = 0, 0, 0, 0, 0

# ピンの設定 例)出力、入力
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin11, GPIO.OUT)#黄色い線-正転・反転用(電流を送ると反転)
GPIO.output(pin11, GPIO.LOW)
GPIO.setup(pin12, GPIO.OUT)#白い線-pwm用(出力をそのまま変更)
GPIO.output(pin12, GPIO.LOW)
GPIO.setup(pin21, GPIO.OUT)#黄色い線-正転・反転用(電流を送ると反転)
GPIO.output(pin21, GPIO.LOW)
GPIO.setup(pin22, GPIO.OUT)#白い線-pwm用(出力をそのまま変更)
GPIO.output(pin22, GPIO.LOW)
GPIO.setup(pin31, GPIO.OUT)#黄色い線-正転・反転用(電流を送ると反転)
GPIO.output(pin31, GPIO.LOW)
GPIO.setup(pin32, GPIO.OUT)#白い線-pwm用(出力をそのまま変更)
GPIO.output(pin32, GPIO.LOW)
GPIO.setup(pin41, GPIO.OUT)#黄色い線-正転・反転用(電流を送ると反転)
GPIO.output(pin41, GPIO.LOW)
GPIO.setup(pin42, GPIO.OUT)#白い線-pwm用(出力をそのまま変更)
GPIO.output(pin42, GPIO.LOW)
GPIO.setup(pin51, GPIO.OUT)#黄色い線-正転・反転用(電流を送ると反転)
GPIO.output(pin51, GPIO.LOW)
GPIO.setup(pin52, GPIO.OUT)#白い線-pwm用(出力をそのまま変更)
GPIO.output(pin52, GPIO.LOW)

pwm1 = GPIO.PWM(pin12, 1000)#pin12, 1000Hzのpwm
pwm2 = GPIO.PWM(pin22, 1000)#pin22, 1000Hzのpwm
pwm3 = GPIO.PWM(pin32, 1000)#pin32, 1000Hzのpwm
pwm4 = GPIO.PWM(pin42, 1000)#pin42, 1000Hzのpwm
pwm5 = GPIO.PWM(pin52, 1000)#pin52, 1000Hzのpwm

pwm1.start(0)#開始,初期出力0
pwm2.start(0)#開始,初期出力0
pwm3.start(0)#開始,初期出力0
pwm4.start(0)#開始,初期出力0
pwm5.start(0)#開始,初期出力0

#　pwmの式
def pwmOutput(start, stop, step, sleep, pwm):
    if step == 0: return#速度を変えないときエラーが出ないようにする
    for i in range(start, stop + (1 if step > 0 else -1), int(step)):
        pwm.ChangeDutyCycle(i)
        time.sleep(sleep)

# programスタート
print("いってらっしゃい！笑\n気をつけてね！笑")

try:
    while Input3 != 9:#9でない場合繰り替えす→9になると終了
        screen.fill((0, 0, 0)) 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    print("おかえり！笑\n無事でよかった！笑")
                    Input3 = 9
                else:
                    print("押されたキー = " + pygame.key.name(event.key))
                    
                    
                """if pygame.key.name(event.key) == "ボタン()":
                    InputM = 1
                    PhaseM += 1
                    print("正転")
                if pygame.key.name(event.key) == "ボタン()":
                    InputM = 2
                    PhaseM += 1
                    print("反転")"""
                
                if pygame.key.name(event.key) == "q":
                    Input1 = 1
                    Phase1 += 1
                    print("巻取り")
                if pygame.key.name(event.key) == "z":
                    Input1 = 2
                    Phase1 += 1
                    print("吐き出し")
                        
                if pygame.key.name(event.key) == "w":
                    Input2 = 1
                    Phase2 += 1
                    print("左回り")
                if pygame.key.name(event.key) == "x":
                    Input2 = 2
                    Phase2 += 1
                    print("右回り")
                
                if pygame.key.name(event.key) == "e":
                    Input3 = 1
                    Phase3 += 1
                    print("閉じる")
                if pygame.key.name(event.key) == "c":
                    Input3 = 2
                    Phase3 += 1
                    print("開く")
                    
                if pygame.key.name(event.key) == "down":
                    Input4 = 1
                    Input5 = 2
                    Phase4 += 1
                    Phase5 += 1
                    print("後進")
                if pygame.key.name(event.key) == "up":
                    Input4 = 2
                    Input5 = 1
                    Phase4 += 1
                    Phase5 += 1
                    print("前進")
                    
                if pygame.key.name(event.key) == "left":
                    Input4 = 1
                    Input5 = 1
                    Phase4 += 1
                    Phase5 += 1
                    print("左旋回")
                if pygame.key.name(event.key) == "right":
                    Input4 = 2
                    Input5 = 2
                    Phase4 += 1
                    Phase5 += 1
                    print("右旋回")
        
            if event.type == KEYUP:  # キーを離したとき
                # ESCキーならスクリプトを終了
                print("離したキー = " + pygame.key.name(event.key))
                    
                """if pygame.key.name(event.key) == "ボタン()":
                    InputM = 0
                    PhaseM -= 1
                    print("停止")
                if pygame.key.name(event.key) == "ボタン()":
                    InputM = 0
                    PhaseM -= 1
                    print("停止")"""
                
                if pygame.key.name(event.key) == "q":
                    Input1 = 0
                    Phase1 -= 1
                    print("停止")
                if pygame.key.name(event.key) == "z":
                    Input1 = 0
                    Phase1 -= 1
                    print("停止")
                    
                if pygame.key.name(event.key) == "w":
                    Input2 = 0
                    Phase2 -= 1
                    print("停止")
                if pygame.key.name(event.key) == "x":
                    Input2 = 0
                    Phase2 -= 1
                    print("停止")
                
                if pygame.key.name(event.key) == "e":
                    Input3 = 0
                    Phase3 -= 1
                    print("停止")
                if pygame.key.name(event.key) == "c":
                    Input3 = 0
                    Phase3 -= 1
                    print("停止")
                    
                if pygame.key.name(event.key) == "down":
                    Input4 = 0
                    Input5 = 0
                    Phase4 -= 1
                    Phase5 -= 1
                    print("停止")
                if pygame.key.name(event.key) == "up":
                    Input4 = 0
                    Input5 = 0
                    Phase4 -= 1
                    Phase5 -= 1
                    print("停止")
                    
                if pygame.key.name(event.key) == "left":
                    Input4 = 0
                    Input5 = 0
                    Phase4 -= 1
                    Phase5 -= 1
                    print("停止")
                if pygame.key.name(event.key) == "right":
                    Input4 = 0
                    Input5 = 0
                    Phase4 -= 1
                    Phase5 -= 1
                    print("停止")
                    
            """pygame.display.update()
        if InputM == 0 or InputM == 9:#停止させる
            pwmOutput(VM, 0, -VM / 25, 0.02, pwmM)#pwm制御をする
            #VM/25(回転していたら100/25で4)ずつ速度を落とす
            VM, RecordM = 0, 0#現在の速度・回転方向を代入
        if InputM == 1:#正転させる
            if RecordM == 2:#反転中の場合一度停止させてから正転させるために
                pwmOutput(VM, 0, -VM / 25, 0.02, pwmM)#停止させる
                VM = 0#このあとの制御のため速度を更新
            GPIO.output(pinM1, GPIO.LOW)#正転させる
            pwmOutput(VM, 100, (100 - VM) / 25, 0.02, pwmM)
            #(100-VM)/25{(100-0)/25=4}ずつ速度を上げる
            VM, RecordM = 100, 1
        if InputM == 2:#反転させる
            if RecordM == 1:#正転中の場合
                pwmOutput(VM, 0, -VM / 25, 0.02, pwmM)
                VM = 0
            GPIO.output(pinM1, GPIO.HIGH)#反転
            pwmOutput(VM, 100, (100 - VM) / 25, 0.02, pwmM)
            VM, RecordM = 100, 2"""
                    
            pygame.display.update()
# 11111111
        if Input1 == 0 or Input1 == 9:#停止させる
            pwmOutput(V1, 0, -V1 / 1, 0.02, pwm1)#pwm制御をする
            #V1/25(回転していたら100/25で4)ずつ速度を落とす
            V1, Record1 = 0, 0#現在の速度・回転方向を代入
        if Input1 == 1:#正転させる
            if Record1 == 2:#反転中の場合一度停止させてから正転させるために
                pwmOutput(V1, 0, -V1 / 1, 0.02, pwm1)#停止させる
                V1 = 0#このあとの制御のため速度を更新
            GPIO.output(pin11, GPIO.LOW)#正転させる
            pwmOutput(V1, 40, (40 - V1) / 1, 0.02, pwm1)
            #(100-V1)/25{(100-0)/25=4}ずつ速度を上げる
            V1, Record1 = 40, 1
        if Input1 == 2:#反転させる
            if Record1 == 1:#正転中の場合
                pwmOutput(V1, 0, -V1 / 1, 0.02, pwm1)
                V1 = 0
            GPIO.output(pin11, GPIO.HIGH)#反転
            pwmOutput(V1, 40, (40 - V1) / 1, 0.02, pwm1)
            V1, Record1 = 40, 2
            
# 22222222
        if Input2 == 0 or Input2 == 9:#停止させる
            pwmOutput(V2, 0, -V2 / 1, 0.02, pwm2)#pwm制御をする
            #V2/25(回転していたら100/25で4)ずつ速度を落とす
            V2, Record2 = 0, 0#現在の速度・回転方向を代入
        if Input2 == 1:#正転させる
            if Record2 == 2:#反転中の場合一度停止させてから正転させるために
                pwmOutput(V2, 0, -V2 / 1, 0.02, pwm2)#停止させる
                V2 = 0#このあとの制御のため速度を更新
            GPIO.output(pin21, GPIO.LOW)#正転させる
            pwmOutput(V2, 100, (100 - V2) / 1, 0.02, pwm2)
            #(100-V2)/25{(100-0)/25=4}ずつ速度を上げる
            V2, Record2 = 100, 1
        if Input2 == 2:#反転させる
            if Record2 == 1:#正転中の場合
                pwmOutput(V2, 0, -V2 / 1, 0.02, pwm2)
                V2 = 0
            GPIO.output(pin21, GPIO.HIGH)#反転
            pwmOutput(V2, 100, (100 - V2) / 1, 0.02, pwm2)
            V2, Record2 = 100, 2
        
# 33333333
        if Input3 == 0 or Input3 == 9:#停止させる
            pwmOutput(V3, 0, -V3 / 1, 0.02, pwm3)#pwm制御をする
            #V3/25(回転していたら100/25で4)ずつ速度を落とす
            V3, Record3 = 0, 0#現在の速度・回転方向を代入
        if Input3 == 1:#正転させる
            if Record3 == 2:#反転中の場合一度停止させてから正転させるために
                pwmOutput(V3, 0, -V3 / 1, 0.02, pwm3)#停止させる
                V3 = 0#このあとの制御のため速度を更新
            GPIO.output(pin31, GPIO.LOW)#正転させる
            pwmOutput(V3, 100, (100 - V3) / 1, 0.02, pwm3)
            #(100-V3)/25{(100-0)/25=4}ずつ速度を上げる
            V3, Record3 = 100, 1
        if Input3 == 2:#反転させる
            if Record3 == 1:#正転中の場合
                pwmOutput(V3, 0, -V3 / 1, 0.02, pwm3)
                V3 = 0
            GPIO.output(pin31, GPIO.HIGH)#反転
            pwmOutput(V3, 100, (100 - V3) / 1, 0.02, pwm3)
            V3, Record3 = 100, 2
            
# 44444444
        if Input4 == 0 or Input4 == 9:#停止させる
            pwmOutput(V4, 0, -V4 / 1, 0.02, pwm4)#pwm制御をする
            #V4/25(回転していたら100/25で4)ずつ速度を落とす
            V4, Record4 = 0, 0#現在の速度・回転方向を代入
        if Input4 == 1:#正転させる
            if Record4 == 2:#反転中の場合一度停止させてから正転させるために
                pwmOutput(V4, 0, -V4 / 1, 0.02, pwm4)#停止させる
                V4 = 0#このあとの制御のため速度を更新
            GPIO.output(pin41, GPIO.LOW)#正転させる
            pwmOutput(V4, 100, (100 - V4) / 1, 0.02, pwm4)
            #(100-V4)/25{(100-0)/25=4}ずつ速度を上げる
            V4, Record4 = 100, 1
        if Input4 == 2:#反転させる
            if Record4 == 1:#正転中の場合
                pwmOutput(V4, 0, -V4 / 1, 0.02, pwm4)
                V4 = 0
            GPIO.output(pin41, GPIO.HIGH)#反転
            pwmOutput(V4, 100, (100 - V4) / 1, 0.02, pwm4)
            V4, Record4 = 100, 2
            
# 55555555
        if Input5 == 0 or Input5 == 9:#停止させる
            pwmOutput(V5, 0, -V5 / 1, 0.02, pwm5)#pwm制御をする
            #V5/25(回転していたら100/25で4)ずつ速度を落とす
            V5, Record5 = 0, 0#現在の速度・回転方向を代入
        if Input5 == 1:#正転させる
            if Record5 == 2:#反転中の場合一度停止させてから正転させるために
                pwmOutput(V5, 0, -V5 / 1, 0.02, pwm5)#停止させる
                V5 = 0#このあとの制御のため速度を更新
            GPIO.output(pin51, GPIO.LOW)#正転させる
            pwmOutput(V5, 100, (100 - V5) / 1, 0.02, pwm5)
            #(100-V5)/25{(100-0)/25=4}ずつ速度を上げる
            V5, Record5 = 100, 1
        if Input5 == 2:#反転させる
            if Record5 == 1:#正転中の場合
                pwmOutput(V5, 0, -V5 / 1, 0.02, pwm5)
                V5 = 0
            GPIO.output(pin51, GPIO.HIGH)#反転
            pwmOutput(V5, 100, (100 - V5) / 1, 0.02, pwm5)
            V5, Record5 = 100, 2
                    
# プログラム強制終了時にモーターを止める                        
except KeyboardInterrupt:
    pass
finally:
    pwm1.stop()
    GPIO.output(pin11, GPIO.LOW)
    pwm2.stop()
    GPIO.output(pin21, GPIO.LOW)
    pwm3.stop()
    GPIO.output(pin31, GPIO.LOW)
    pwm4.stop()
    GPIO.output(pin41, GPIO.LOW)
    pwm5.stop()
    GPIO.output(pin51, GPIO.LOW)
    GPIO.cleanup()
    sys.exit()