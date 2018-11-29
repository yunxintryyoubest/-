###################超级用户界面
from  conf import  settings
import  json,os,sys
import configparser
# from  conf import settings
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
# sys.path.append(PATH)
# print('admin_path这个绝对路径是:',PATH)
# print('导入admin账户成功')
from  admin_user import *
f_open=open('account_data.txt','r')
Dicyionary=json.loads(f_open.read())
################这个是一个字典形式
class admin:
    print('进入超级用户端..........')
    print('请进入身份验证............')
    admin_menus_start_choices='''
    1,'直接登录',
    2,'注册'
    '''
    print(admin_menus_start_choices)
    admin_menus_start_choices_choice=input('请输入你的选择:')
    ##########################登录页面#####################################
    if admin_menus_start_choices_choice==str(1):
        print('进入登录页面....................')
        fh = open('account_data.txt', 'r')
        has_registered_admin_data=json.loads(fh.read())
        print(has_registered_admin_data)
        print(type(has_registered_admin_data))

        input_admin_username = input('请输入账号：')
        input_admin_keyword = str(input('请输入密码：'))
        input_data = {}
        input_data[input_admin_username] = input_admin_keyword
        print(input_data)
        print(len(has_registered_admin_data))
        i=0
        for i in range(0,len(has_registered_admin_data)):
            if input_data ==  has_registered_admin_data[i]:
                print('用户匹配成功')
                print('身份验证成功')
                print('欢迎管理员【{}】进入后台管理系统............'.format(input_admin_username))
                print('welcome  to admin 界面...................')
                admin_menus = '''
                          1,'查看'
                          2,'搜索',
                          3,'管理,
                          4'账户信息'''
                print(admin_menus)
                admin_menu_choice=input('请输入你要选择的操作:')
                if admin_menu_choice == str(1):
                    from  admin_user import look_informations
                    look_informations.all_informations()
                    break
                elif admin_menu_choice==str(2):
                    from  admin_user import admin_search
                    admin_search.admin_serach()
                    break
                elif admin_menu_choice == str(4):
                    # print('进入账户信息界面')
                    from  admin_user  import  admin_user_personal_information
                    admin_user_personal_information.admin_personal_information()
                    break
                elif admin_menu_choice==str(3):
                    from  admin_user import admin_manage
                    admin_manage.admin_manage()
                    break
                else:
                    print('认证失败')
                    break
            else:
                continue
        else:
            print('身份验证失败')
















        ########################注册页面
    elif admin_menus_start_choices_choice==str(2):
        print('进入注册页面')
        account={}
        admin_username=input('请输入你要添加的admin账号：')
        admin_keyword=input('请输入你要添加的admin密码：')
        account[admin_username]=admin_keyword
        Dicyionary.append(account)
        account_data_str=json.dumps(Dicyionary)
        f = open('account_data.txt', 'w')
        f.write(account_data_str)
        f.close()
        # dic1 = open('account_data.txt', 'r')
        # all_data = json.loads(dic1.read())
        # print(all_data)
        # print('已经添加成功')
        print('注册成功')


















