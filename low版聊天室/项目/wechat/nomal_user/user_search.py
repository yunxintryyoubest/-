#############################进入搜索用户和群的界面
QQ_IP = open('ip_save.txt', 'r')
QQ_IP = QQ_IP.read()
print('已经取到这个ip地址：', QQ_IP)
class search:
    def __init__(self):
        import socket
        sk = socket.socket()
        self.sk = sk
        sk.connect((QQ_IP, 8080))
        print('欢迎进入seach界面')
        search_menus = '''
          1,在线搜
          2,本地搜索
          '''
        print(search_menus)
        self.main_search()
    def main_search(self):
        search_menus_choice = input('请输入你的选择：')
        if search_menus_choice == str(1):
            print('您选择了在线搜索')
            search_number = input('请输入你要搜索的QQ号（用户，群等）')
            self.sk.send(search_number.encode('utf-8'))


            QQ_number=self.sk.recv(1024)
            print('已经找到这个QQ号码',QQ_number)

        elif search_menus_choice == str(2):
            print('您选择了本地搜索')
            search_number_choice='''
            1,查看你的ip地址
            2,搜索本地好友
            '''
            search_number = input('请输入你要搜索（本地）的QQ号（用户，群等）')
            if search_number==str(1):
                print('你的ip地址是:',QQ_IP)
            elif search_number==str(2):
                print('please wait..............')


        else:
            print('不存在，输入有误')






