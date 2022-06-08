import serial
import time
 
ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)
 
for i in range(50):
    # Reading all bytes available bytes till EOL
    line = ser.readline() 
    if line:
        # Converting Byte Strings into unicode strings
        string = line.decode()  
        # Converting Unicode String into integer
        num = int(string) 
        print(num)
 
ser.close()