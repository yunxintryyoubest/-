


##############################主菜单界面################################################
###############导入这个settings，引入绝对路径
class main_choice:
    def __init__(self):
        print ('进入main主界面')
        menu_choice = input("请输入你的选择:")
        if menu_choice==str(1):
            self.admin()
        if menu_choice==str(2):
            self.nomal_user()
        if menu_choice==str(3):
            self.exit()


    def admin(self):
        # print('欢迎进入admin界面')
        from core import  admin
        admin.admin()

    def nomal_user(self):
        from nomal_user import  client
        client.client_main()

    def exit(self):
        print('你已经选择了退出界面')
        exit()








