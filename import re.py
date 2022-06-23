import re, os,shutil
destination = r'C:\Users\anifa\Desktop\GITB\R-Pi'
txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# x = re.findall()
date = "Data_logger_782184807821_16_06_2022.csv"
pattern = re.findall("(_[0-9]|1[0-9]|2[0-9]|3[0-5])_([0-9]|1[0-9]|2[0-9]|3[0-5])_([0-9][0-9][0-9][0-9])", date)
# x=pattern.findall(destination)
print(pattern)
# if x:
#   print("YES! We have a match!")
#   print(x)
# else:
#   print("No match")