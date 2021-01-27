from gpiozero import LED
from time import sleep

yellow = LED(3) # 3はGPIOの番号

while True:
    yellow.on()
    sleep(0.4)
    yellow.off()
    sleep(0.4)