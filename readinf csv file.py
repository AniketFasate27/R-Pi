import matplotlib.pyplot as plt
import csv
  
# x = []
# y = []
x = []
t = []
h = []
f= []
hic = []  

fig = plt.figure('Data Logger')
# fig.suptitle('Data Logger', fontsize = 20)
ax = fig.add_subplot(2,2,1)
ay = fig.add_subplot(2,2,2)
az = fig.add_subplot(2,2,3)
aa = fig.add_subplot(2,2,4)

with open('Data_logger_782184807821_17_06_2022.csv','r',newline ='\n') as csvfile:
    heading = next(csvfile)
    lines = csv.reader(csvfile)

    
    # lines = csv.reader(csvfile, delimiter=',')

    for row in lines:

        print(row)
        # x.append(row[0])             
        # t.append(float(row[1]))
        # h.append(float(row[2]))
        # f.append(float(row[3]))
        # hic.append(float(row[4]))
        



# x=x[-15:]   
# t=t[-15:]
# h=h[-15:]
# f=f[-15:]
# hic=hic[-15:]

# ax.plot(x,t,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='blue',markersize=3,label = "Temp")
# ax.set_title('Humidity')
# ax.set_ylim([0,max(t)+10])

# ay.plot(x,h,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='green',markersize=3,label = "Humi")
# ay.set_title('Temprature')
# ay.set_ylim([0,max(h)+10])


# az.plot(x,f,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='red',markersize=3,label = "HI")
# az.set_title('Heat Index')
# az.set_ylim([0,max(f)+10])


    
# aa.plot(x,hic,color='black',linestyle='dashed',linewidth=1,marker ='o',markerfacecolor='yellow',markersize=3,label = "Lux")
# aa.set_title('Lux')
# aa.set_ylim([0,max(hic)+10])

# plt.tight_layout()
# # plt.grid()
# plt.legend()
# plt.show()










# plt.plot(x, t, color = 'g', linestyle = 'dashed',
#          marker = 'o',label = "Weather Data")
  
# plt.xticks(rotation = 25)
# plt.xlabel('Dates')
# plt.ylabel('Temperature(°C)')
# plt.title('Weather Report', fontsize = 20)
# plt.grid()
# plt.legend()
# plt.show()