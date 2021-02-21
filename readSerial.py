import serial
import time
from serial import Serial
ser = serial.Serial('COM4', 115200, timeout=0) 

while 1:
   data=ser.readline()
   print data
   #f = open('myfile.txt','w') 
   #data=str(data)
   #f.write(data)
   #f.close()
   time.sleep(1) 