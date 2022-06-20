import matplotlib.pyplot as plt
import matplotlib.animation as animation

from datetime import datetime


import csv
import serial
import time
import os.path
fields =['Time', 'Humidity', 'Temprature', 'HI', 'Lux']
header ="id, Humidity, Temprature, HI, Lux"
# field names 

now = datetime.now()

ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)
z=1
x = []
t = []
h = []
f= []
hic = []
data = []

fig = plt.figure('Data Logger')
# fig.suptitle('Data Logger', fontsize = 20)
ax = fig.add_subplot(2,2,1)
ay = fig.add_subplot(2,2,2)
az = fig.add_subplot(2,2,3)
aa = fig.add_subplot(2,2,4)
# for i in range(50):

def animate(i, x, t, h, f, hic):
    
    # Reading all bytes available bytes till EOL
    line = ser.readline() 
    if line:
        # Converting Byte Strings into unicode strings
        # string = line.decode()  
        # Converting Unicode String into integer
        line_as_list = line.split(b',')

        i = line_as_list[0].decode()
        temp = line_as_list[1]
        hum = line_as_list[2]
        far = line_as_list[3]
        farhic = line_as_list[4]

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%d_%m_%Y")


        relProb_as_list_1 = temp.split(b'\n')
        relProb_as_list_2 = hum.split(b'\n')
        relProb_as_list_3 = far.split(b'\n')
        relProb_as_list_4 = farhic.split(b'\n')
    
        relProb_float_1 = float(relProb_as_list_1[0])
        relProb_float_2 = float(relProb_as_list_2[0])
        relProb_float_3 = float(relProb_as_list_3[0])
        relProb_float_4 = float(relProb_as_list_4[0])
    
        data.append(current_time)
        data.append(relProb_float_1)
        data.append(relProb_float_2)
        data.append(relProb_float_3)
        data.append(relProb_float_4)

        

        if((os.path.exists("Data_logger_" +i+"_"+current_date+".csv")==False)):
            with open("Data_logger_" +i+"_"+current_date+".csv",'x')as write_obj:
                # print('Creating new file and appending data')
                csv_writer =csv.writer(write_obj)
                csv_writer.writerow(fields)
                csv_writer.writerow(data)
                
                print(data)
                data.clear()    
            
        else:
            with open("Data_logger_" +i+"_"+current_date+".csv",'a+')as write_obj:
                # print('previous file exists')
                csv_writer = csv.writer(write_obj)
            
                csv_writer.writerow(data)
                # print(write_obj)
                data.clear()

        
        with open("Data_logger_" +i+"_"+current_date+".csv",'r',newline ='\n') as csvfile:
            heading = next(csvfile)
            lines = csv.reader(csvfile)
   
            # lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                # print(row)
                x.append(row[0])             
                t.append(float(row[1]))
                h.append(float(row[2]))
                f.append(float(row[3]))
                hic.append(float(row[4]))


        x=x[-15:]   
        t=t[-15:]
        h=h[-15:]
        f=f[-15:]
        hic=hic[-15:]

        ax.clear()
        ay.clear()
        ay.clear()
        az.clear()
        aa.clear()
            
        ax.plot(x,t,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='blue',markersize=4,label = "Temp")
        ax.set_title('Humidity')
        ax.set_ylim([0,max(t)+10])
        
        ay.plot(x,h,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='green',markersize=4,label = "Humi")
        ay.set_title('Temprature')
        ay.set_ylim([0,max(h)+10])

       
        az.plot(x,f,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='red',markersize=4,label = "HI")
        az.set_title('Heat Index') 
        az.set_ylim([0,max(f)+10])

        
        aa.plot(x,hic,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='yellow',markersize=4,label = "Lux")
        aa.set_title('Lux')
        aa.set_ylim([0,max(hic)+10])

        plt.tight_layout()
       

ani = animation.FuncAnimation(fig, animate, fargs=(x, t, h, f, hic), interval=1)
plt.show()
	 
# ser.close()










