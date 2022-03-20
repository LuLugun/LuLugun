import os
import zipfile
import math

def zip_to_file(n):
    zf = zipfile.ZipFile('E:\\20220221\\VID_20220217_171300_'+str(n)+'.zip', 'w', zipfile.ZIP_DEFLATED)

    for i in range((n-1)*1000,n*1000):
        file_name = 'VID_20220217_171300_'+str(i+1)+'.jpg'
        zf.write(os.path.join('E:\\20220221\\jpg\\', file_name))

for i in range(1,5):
    zip_to_file(i)