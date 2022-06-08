import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [22,25,26,28,26,30,50]
z = [23,33,33,22,22,55,67]


plt.figure()
# plt.rcParams["figure.figsize"] = (20,10)
plt.subplot(2,2,1)
plt.plot(x,y,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='blue',markersize=8,label = "Temp")

plt.xlabel('Time')
plt.ylabel('Temprature')
plt.legend()
plt.subplot(2,2,2)
plt.plot(x,z,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='green',markersize=8,label = "Humi")
plt.xlabel('Time')
plt.ylabel('Humidity')
plt.legend()

plt.subplot(2,2,3)
plt.plot(x,z,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='red',markersize=8,label = "HI")
plt.xlabel('Time')
plt.ylabel('HI')
plt.legend()

plt.subplot(2,2,4)
plt.plot(x,z,color='black',linestyle='dashed',linewidth=2,marker ='o',markerfacecolor='yellow',markersize=8,label = "Lux")
plt.xlabel('Time')
plt.ylabel('Lux')
plt.legend()

plt.show()