import datetime
import picamera
import smbus
import time

camera = picamera.PiCamera()

def takepic():
    camera.resolution = (600,800)
    camera.rotation = 270
    camera.start_preview()

    # Camera warm-up time 
    now = datetime.datetime.now()
    #picname = f"pic/{dt.year}{dt.month}{dt.day}-{dt.hour}-{dt.minute}.png"                                        
    picname = f"pic/"+ now.strftime("%Y%m%d-%H%M") +".png"                                        
    time.sleep(10)
    camera.capture(picname)
    return picname

i2c = smbus.SMBus(1)
addr = 0x38
config = 0b11000110
 
#i2c.write_byte_data(addr, 0x40, 0x80) #reset
#i2c.write_byte_data(addr, 0x41, config)
#time.sleep(0.2)

def getLightSensorValues():
    data = i2c.read_i2c_block_data(addr,0x44,6)
    PS = data[1]*256 + data[0] 
    ALS_DATA0 = data[3]*256 + data[2]
    ALS_DATA1 = data[5]*256 + data[4]

    return PS, ALS_DATA0, ALS_DATA1
      
#main
while True:
    picname = takepic()
    #PS, ALS_DATA0, ALS_DATA1 = getLightSensorValues()
    #print(PS,ALS_DATA0,ALS_DATA1,picname , sep = ",")
    print(picname , sep = ",")
    time.sleep(60)
