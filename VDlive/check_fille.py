import os
import datetime

local_path = os.path.dirname(os.path.abspath(__file__))
#mypath = input('請輸入檔案路徑:')
mypath = local_path+'//xml//'
files = os.listdir(mypath)
start_time = files[0].replace('VDLiveList.xml','')
start_time = datetime.datetime.strptime(start_time[0:-3], "%Y%m%d_%H_%M")
print('start:',start_time)
f = open('lose_file.txt', 'w')

for file in files:
    file = file.replace('VDLiveList.xml','')
    file = datetime.datetime.strptime(file[0:-3], "%Y%m%d_%H_%M")
    if file == start_time:
        start_time = start_time + datetime.timedelta(minutes=1)
    else:
        while True:
            if file == start_time:
                start_time = start_time + datetime.timedelta(minutes=1)
                break
            print('lose:',start_time)
            start_time_str = datetime.datetime.strftime(start_time, "%Y%m%d_%H_%M")
            f.write(start_time_str+'\n')
            start_time = start_time + datetime.timedelta(minutes=1)
f.close()