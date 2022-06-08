import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

#initialize serial port
ser = serial.Serial()
# ser.port = '/dev/ttyACM0' #Arduino serial port
ser.port = 'COM3' #Arduino serial port
ser.baudrate = 115200
ser.timeout = 1 #specify timeout when using readline()
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
ay = fig.add_subplot(2,2,2)
xs = [] #store trials here (n)
ys = [] #store relative frequency here
rs = [] #for theoretical probability

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    #Aquire and parse data from serial port
    line=ser.readline()      #ascii
    if line:
        line_as_list = line.split(b',')
        i = int(line_as_list[0])
        relProb = line_as_list[1]
        relProb_as_list = relProb.split(b'\n')
        relProb_float = float(relProb_as_list[0])
	
	# Add x and y to lists
        xs.append(i)
        ys.append(relProb_float)
        # rs.append(0.5)
        

        xs.append(i)
        rs.append(relProb)
        # rs.append(0.5)
        print(xs)
        print(ys)
        print(rs)



    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    #ys = ys[-20:]

    # Draw x and y lists
        ax.clear()
        ay.clear()
        ax.plot(xs, ys, label="Experimental Probability")
        # ax.plot(xs, rs, label="Theoretical Probability")
        # ay.plot(xs, rs, label="Theoretical Probability")

    # Format plot
        plt.xticks(rotation=45, ha='right')
        # plt.subplots_adjust(bottom=0.30)
        plt.title('DATA LOGGER ')
        plt.ylabel('Relative frequency')
        plt.legend()
        plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
    #plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

        ay.plot(xs, rs, label="Theoretical Probability")
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('DATA LOGGER ')
        plt.ylabel('Relative frequency')
        plt.legend()
        plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=0)
plt.show()