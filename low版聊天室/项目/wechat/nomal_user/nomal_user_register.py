####################进入普通用户注册页面################################################

import  os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
import demjson
register_ip=[]
# open('ip_save.txt','r')





class normal_user_register:
    def start():
        print('进入普通用户注册页面....................................')

        ####################走服务端这块,进行验证#####################################################################
        import socket
        sk = socket.socket()
        sk.connect(('127.0.0.1', 8080))
        try:
            while True:
                normal_user_number = input('请输入你想注册的手机号码:')
                if len(normal_user_number) == 3:
                    print('可以通过')
                    break
                else:
                    print('号码请重新输入，3位....................................')
                    continue
            normal_user_password = str(input('请输入密码：'))
            normal_user_dict={}
            normal_user_dict[normal_user_number]=normal_user_password

            print(normal_user_dict)
            sk.send(str(normal_user_dict).encode('utf-8'))
            print('已经发送')
            data = sk.recv(1024)
            print('服务端发回消息.................................................................')
            print('接收到服务端的数据是:',data.decode('utf-8'))
            import time
            # time.sleep(10000)
            print('您的QQ号是', data.decode('utf-8'))
            QQ_personal_data = data.decode('utf-8')
            print(QQ_personal_data)
            ###########创建文件夹
            import os
            # os.mkdir('C:/Users/Public/Documents/{}.txt'.format(QQ_personal_data))
            # QQ_docu = open('C:/Users/Public/Documents/' + '{}'.format(QQ_personal_data) + ".txt", 'w')
            QQ_docu = open('{}'.format(QQ_personal_data) + ".txt", 'w')
            QQ_docu.write(QQ_personal_data)
            print('写入文件')
            QQ_docu.close()
#############################在main首页取这个登录的QQ号码###########################################################
            docu=open('QQ_ID_docu'+'.txt','w')
            docu.write(QQ_personal_data)
            docu.close()
            ip_quest='iq_request'
            sk.send(str(ip_quest).encode('utf-8'))
            print('已经发送出去了这个请求ip的信息')
            ###########拿到这个ip地址#####################################################
            # time.sleep(2)
            IP_recv = sk.recv(1024).decode('utf-8')
            print('接收到这个IP地址是：',IP_recv)
            ip_open=open('ip_save.txt','r')
            ip_open_data=ip_open.read()
            ip_open_data=None
            print('已经置空')
            ip_open.close()
            ip_save_read = open('ip_save.txt', 'w')
            ip_save_read.write(str(IP_recv))
            ip_save_read.close()
            # sk.close()
            print('已经关闭这个QQ注册环节')
            import time
            # time.sleep(1)
            #####################将这个ip对空，重新置入对应的ip地址########################################################################
            from  nomal_user import new_nomal_user_main
            # nomal_user_main.normal_user_main()
            new_nomal_user_main.new_nomal_user()
        except Exception as e:
            print(e)
normal_user_register.start()


