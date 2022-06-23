import os
# import glob
import re
files_writtern=[]
# List all files in a directory using scandir()
# basepath = 'Users\anifa\Desktop\GITB\R-Pi/'
# print(os.listdir(path='.'))

for filename in os.listdir():
    if filename.endswith('.csv'):
        files_writtern.append(filename)

# print(files_writtern)
files_with_date=[]
sending = ""
com_date = "16_06_2022"
print(type(com_date))
for i in files_writtern:
    x=re.findall(com_date,i)
    if x:
        files_with_date.append(i)


sending = ",".join(map(str,files_with_date))  
print(sending)




