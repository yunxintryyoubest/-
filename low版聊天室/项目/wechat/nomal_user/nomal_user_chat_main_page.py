##############################这里是配置这个用户聊天的界面#################################################
print('&'*1000)
print('欢迎来到这个用户聊天的主界面')
import os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
print(PATH)
import socket
import demjson
import json
import os,sys
#######################################拿到自己的ip到主界面去
f_open = open('QQ_ID_docu.txt', 'r')
all_dic_data = json.loads(f_open.read())
QQ_ID = all_dic_data

print('这个QQ的id是：',QQ_ID)
f_open.close()
with open(('{}/nomal_user/nomal_all_ip_data/chat_main_ip/{}_main.txt'.format(PATH, QQ_ID)), 'r')as f:
    main_ip=f.read()
    f.close()

print('这个用户自己的ip是:',main_ip)
class main_chat_nomal_user:
    def __init__(self):
        print('开始进入这个聊天的主界面了')
        import socket
        sk = socket.socket()
        sk.connect((main_ip, 8080))
        self.sk=sk
        self.main_start()
    def main_start(self):
        number = input('请输入好友QQ号码：')
        self.sk.send(str(number).encode('utf-8'))
        print('已经发送出去')

        friend_ip=self.sk.recv(1024).decode('utf-8')
        print(friend_ip)



        if not os.path.exists('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}'.format(PATH, QQ_ID)):
            os.mkdir('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}'.format(PATH, QQ_ID))
        open(('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}/chat.txt'.format(PATH, QQ_ID)), 'w')
        with open(('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}/chat.txt'.format(PATH, QQ_ID)), 'w')as f:
            f.write(str(friend_ip))
            f.close()
        with open(('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}/chat_ID.txt'.format(PATH, QQ_ID)), 'w')as f:
            f.write(str(number))
            f.close()

        print('保存成功')
        import time
        # time.sleep(1000)
        from nomal_user import nomal_user_chat_others
        nomal_user_chat_others.nomal_user_chat_others()



main_chat_nomal_user()



























































