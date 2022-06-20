from urllib.request import urlretrieve
import time
import os

# 操作：（python3环境)
# 在检查中找到img src项，将其url弄下来
# 此url中有一个pageid=1,将数字换成{}
# 此字符串为参数url，页码尾数为tail_id, 保存文件夹目录为dirpath
# 参数输入到函数szsy_get中即可

url = 'http://162.105.138.126/OnLineReader/command/imagepage.ashx?objID=obj201409267qul6pld1gs390nn0000058167&metaId=meta201407027qul6pld00000520869&OrgId=apabi_usp&Ip=undefined&scale=1.7611447113873502&width=5054&height=7240&pageid={}&ServiceType=Imagepage&scaleType=1&OrWidth=663.999883910117&OrHeight=951.999888201652&testres=&debug=&SessionId=B61D3955674FFB04&UserName=%E8%83%A1%E5%BF%97%E6%96%8C&cult=CN&rights=1-0_00&time=2022-06-20%2014:59:43&sign=410F5631A58BC4E036FAB2B2DA607A3F'

tail_id = 6
dirpath = 'download_test'


def szsy_get(url, tail_id, dirpath):
    print('start {}'.format(dirpath))
    if os.access(dirpath, os.R_OK) == False:
        os.makedirs(dirpath)
    try:
        for i in range(tail_id):
            url_use = url.format(i+1)
            urlretrieve(url_use, "{}/{}.png".format(dirpath,i+1))
            print('{} Done'.format(i+1))
    except:
        print('failed somehow')

szsy_get(url, tail_id, dirpath)
