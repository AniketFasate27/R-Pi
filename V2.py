import matplotlib.pyplot as plt
import matplotlib.animation as animation


import serial
import time

ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)
z=1
x = []
y = []
z = []
fig = plt.figure()
ax = fig.add_subplot(2,2,1)
ay = fig.add_subplot(2,2,2)

# for i in range(50):
def animate(i, x, y):
    
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
        relProb = line_as_list[1]
        # print(i)
            
        relProb_as_list = relProb.split(b'\n')
            
        relProb_float = int(relProb_as_list[0])
        # print(relProb_float)

        y.append(relProb_float)
        x.append(i)
        print(' '.join(map(str,x)))
        print(' '.join(map(str,y)))
        # print(len(x))
        # print(len(y))
            

        ax.clear()
        ay.clear()

        # plt.figure()
        # plt.rcParams["figure.figsize"] = (20,10)
        # plt.subplot(2,2,1)
        # ax.plot(x,y, label="Data Logger")
        

            
        ax.plot(x,y,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='blue',markersize=8,label = "Temp")
        plt.xticks(rotation=45, ha='right')    
        plt.xlabel('Time')
        plt.ylabel('Temprature')
        plt.legend()
        # plt.axis([1, None, 0, 1.1])

        # plt.subplot(2,2,2)
        # plt.plot(x,z,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='green',markersize=8,label = "Humi")
        # plt.xlabel('Time')
        # plt.ylabel('Humidity')
        # plt.legend()




        # plt.subplot(2,2,3)
        # plt.plot(x,z,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='red',markersize=8,label = "HI")
        # plt.xlabel('Time')
        # plt.ylabel('HI')
        # plt.legend()

        # plt.subplot(2,2,4)
        # plt.plot(x,z,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='yellow',markersize=8,label = "Lux")
        # plt.xlabel('Time')
        # plt.ylabel('Lux')
        # plt.legend()


ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=0)
plt.show()
	


 
# ser.close()










