# fp = open('sales_3.txt', 'w')
# for i in range(1,10):
#     fp.write('first line' + ','+'Second line'+','+'dfndfv')
#     fp.write('\n')


try:
    file_path = r'C:\Users\anifa\Desktop\GITB\R-Pi\sales_5.text'
    # create file
    with open(file_path, 'x') as fp:
        print('file not exit')
        # fp = open('sales_5.txt', 'w')
        
        pass
except:
    print('File already exists')

