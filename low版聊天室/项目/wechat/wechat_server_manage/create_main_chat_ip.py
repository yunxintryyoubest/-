

import random
import re
import demjson,os,sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
# from  wechat_server_manage import test

# QQ_ID = test.create_id.create()
def has_ip():
    # ip_addr = self.create_ip()
    # print('生成ip地址。。。。。。。。。。。。。。。。。。。。。。。')
    # ip_addr='192.168.2.55'
    third_last_ip=int(random.randrange(100))
    last_ip = int(random.randrange(200))
    # print(last_ip)
    seconde_last_ip = int(random.randrange(255))
    # print(seconde_last_ip)
    ip_addr = '127.{}.{}.{}'.format(third_last_ip,seconde_last_ip, last_ip)
    # print('这个生成的ip地址是：', ip_addr)
    exist_ip = open('QQ_ID_IP_save.txt', 'r')
    existed_ip = exist_ip.read()
    exist_ip.close()
    existed_ip = demjson.decode(existed_ip)
    # print('全部的ip地址是：', existed_ip)
    # print(type(existed_ip))
    existip = []
    for i in range(0, len(existed_ip)):
        (key, value), = existed_ip[i].items()
        existip.append(value)
        # if ip_addr ==value:
        #     print('已经存在这个ip')
    if ip_addr in existip:
        print('已经存在这个ip')
        return value

    else:
        # print('这个ip不存在，no one is usering ')
        return ip_addr
# ip=has_ip()
# print('>'*1000)
# print(ip)