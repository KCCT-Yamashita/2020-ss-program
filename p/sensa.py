import smbus            # use I2C
import math
from time import sleep  # time module
import cv2
import numpy as np

### define #############################################################
DEV_ADDR = 0x68         # device address
PWR_MGMT_1 = 0x6b       # Power Management 1
ACCEL_XOUT = 0x3b       # Axel X-axis
ACCEL_YOUT = 0x3d       # Axel Y-axis
ACCEL_ZOUT = 0x3f       # Axel Z-axis
TEMP_OUT = 0x41         # Temperature
GYRO_XOUT = 0x43        # Gyro X-axis
GYRO_YOUT = 0x45        # Gyro Y-axis
GYRO_ZOUT = 0x47        # Gyro Z-axis

MSIZE = 256 #表示のサイズ
 
# 1byte read
def read_byte( addr ):
    return bus.read_byte_data( DEV_ADDR, addr )
 
# 2byte read
def read_word( addr ):
    high = read_byte( addr   )
    low  = read_byte( addr+1 )
    return (high << 8) + low
 
# Sensor data read
def read_word_sensor( addr ):
    val = read_word( addr )
    if( val < 0x8000 ):
        return val # positive value
    else:
        return val - 65536 # negative value
 
# Get Temperature
def get_temp():
    temp = read_word_sensor( TEMP_OUT )
    # offset = -521 @ 35℃
    return ( temp + 521 ) / 340.0 + 35.0
 
# Get Gyro data (rimg = np.full((210, 425, 3), 128, dtype=np.uint8)aw value)
def get_gyro_data_lsb():
    x = read_word_sensor( GYRO_XOUT )
    y = read_word_sensor( GYRO_YOUT )
    z = read_word_sensor( GYRO_ZOUT )
    return [ x, y, z ]
# Get Gyro data (deg/s)
def get_gyro_data_deg():
    x,y,z = get_gyro_data_lsb()
    # Sensitivity = 131 LSB/(deg/s), @ccv2.destroyAllWindows()f datasheet
    x = x / 131.0
    y = y / 131.0
    z = z / 131.0
    return [ x, y, z ]
 
# Get Axel data (raw value)
def get_accel_data_lsb():
    x = read_word_sensor( ACCEL_XOUT )
    y = read_word_sensor( ACCEL_YOUT )
    z = read_word_sensor( ACCEL_ZOUT )
    return [ x, y, z ]
# Get Axel data (G)
def get_accel_data_g():
    x,y,z = get_accel_data_lsb()
    # Sensitivity = 16384 LSB/G, @cf datasheet
    x = x / 16384.0
    y = y / 16384.0
    z = z / 16384.0
    return [x, y, z]
 
###img = np.full((210, 425, 3), 128, dtype=np.uint8) Main function ######################################################
bus = smbus.SMBus( 1 )
bus.write_byte_data( DEV_ADDR, PWR_MGMT_1, 0 )

img = np.zeros((MSIZE,MSIZE+MSIZE,3), np.uint8)    #画像window

while 1:
    temp = get_temp()
    print( 't= %.2f' % temp, '\t'),
    img = np.zeros((MSIZE,MSIZE+MSIZE,3), np.uint8)
#    gyro_x,gyro_y,gyro_z = get_gyro_data_deg()
#    print( 'Gx= %.3f' % gyro_x, '\t'),
#    print( 'Gy= %.3f' % gyro_y, '\t'),
#    print( 'Gz= %.3f' % gyro_z, '\t'),

    accel_x,accel_y,accel_z = get_accel_data_g()
    th_x=math.atan(accel_x/math.sqrt(accel_y*accel_y+accel_z*accel_z))
    th_y=math.atan(accel_y/math.sqrt(accel_x*accel_x+accel_z*accel_z))
    th_z=math.atan(accel_z/math.sqrt(accel_x*accel_x+accel_y*accel_y))

    print( 'Ax= %.3f\t' % accel_x, '\t')
    print( 'Ay= %.3f' % accel_y, '\t',)
    print( 'Az= %.3f' % accel_z, '\t',)
    print('\n') # 改行
    cv2.line(img, (0,int(MSIZE/2-MSIZE/2*math.sin(th_x))),\
      (MSIZE, int(MSIZE/2+MSIZE/2*math.sin(th_x))), \
      (255, 255, 255), thickness=1, lineType=cv2.LINE_4)
    cv2.line(img, (MSIZE,int(MSIZE/2-MSIZE/2*math.sin(th_y))),\
      (MSIZE+MSIZE, int(MSIZE/2+MSIZE/2*math.sin(th_y))), \
      (255, 255, 255), thickness=1, lineType=cv2.LINE_4)
    cv2.imshow('img',img)
    k = cv2.waitKey(1)  #引数は待ち時間(ms)
    if k == 27: #Esc入力時は終了
        break
    sleep( 0.2 )

cv2.destroyAllWindows()