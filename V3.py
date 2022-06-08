import matplotlib.pyplot as plt
import matplotlib.animation as animation


import serial
import time

ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)
z=1
x = []
t = []
h = []
f= []
hic = []


fig = plt.figure()
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
        # num = int(string) 
        # print(num)
        line_as_list = line.split(b',')
        i = int(line_as_list[0])
        temp = line_as_list[1]
        hum = line_as_list[2]
        far = line_as_list[3]
        farhic = line_as_list[4]
        # print(i)
        # print(temp)
        # print(hum)
        # print(far)
        # print(farhic)

        relProb_as_list_1 = temp.split(b'\n')
        relProb_as_list_2 = hum.split(b'\n')
        relProb_as_list_3 = far.split(b'\n')
        relProb_as_list_4 = farhic.split(b'\n')
        # print(relProb_as_list_1)
        # print(relProb_as_list_2)
        # print(relProb_as_list_3)
        # print(relProb_as_list_4)


        relProb_float_1 = float(relProb_as_list_1[0])
        relProb_float_2 = float(relProb_as_list_2[0])
        relProb_float_3 = float(relProb_as_list_3[0])
        relProb_float_4 = float(relProb_as_list_4[0])

        # print(relProb_float_1)
        # print(relProb_float_2)
        # print(relProb_float_3)
        # print(relProb_float_4)

        
        x.append(i)
        t.append(relProb_float_1)
        h.append(relProb_float_2)
        f.append(relProb_float_1)
        hic.append(relProb_float_1)

        print(' '.join(map(str,x)))
        print(' '.join(map(str,t)))
        print(' '.join(map(str,h)))
        print(' '.join(map(str,f)))
        print(' '.join(map(str,hic)))

        # print(len(x))
        # print(len(y))
        x=x[-20:]   
        t=t[-20:]
        h=h[-20:]
        f=f[-20:]
        hic=hic[-20:]

        ax.clear()
        ay.clear()
        ay.clear()
        az.clear()
        aa.clear()

        # plt.figure()
        # plt.rcParams["figure.figsize"] = (20,10)
        # plt.subplot(2,2,1)
        # ax.plot(x,y, label="Data Logger")
        

            
        ax.plot(x,t,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='blue',markersize=4,label = "Temp")
        # plt.xticks(rotation=45, ha='right')    
        ax.set_xlabel('Time')
        # plt.ylabel('Temprature')
        ax.set_ylabel('Temprature')
        ax.legend()
        
        # plt.axis([1, None, 0, 1.1])

        # plt.subplot(2,2,2)
        ay.plot(x,h,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='green',markersize=4,label = "Humi")
        ax.set_xlabel('Time')
        ax.set_ylabel('Humidity')

        # plt.xlabel('Time')
        # plt.ylabel('Humidity')
        ay.legend()




        # plt.subplot(2,2,3)
        az.plot(x,f,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='red',markersize=4,label = "HI")
        ax.set_xlabel('Time')
        ax.set_ylabel('HI')
        
        
        # plt.xlabel('Time')
        # plt.ylabel('HI')
        az.legend()

        # plt.subplot(2,2,4)
        aa.plot(x,hic,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='yellow',markersize=4,label = "Lux")
        ax.set_xlabel('Time')
        ax.set_ylabel('Lux')
        
        # plt.xlabel('Time')
        # plt.ylabel('Lux')
        aa.legend()


ani = animation.FuncAnimation(fig, animate, fargs=(x, t, h, f, hic), interval=0)
plt.show()
	


 
# ser.close()










