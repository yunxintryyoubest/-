
######################################这里是新用户注册成功后登录的页面#######################################

print('欢迎注册本聊天室...............................')
print('#'*200)
for i in range(0,10):
    print(' ' * 10 + '#' * 2 + ' ' * 8 + '#' * 5 + ' ' * 9 + '#' * 2)
    print(' ' * 11 + '#' * 2 + ' ' * 5 + '#' * 2 + ' ' * 5 + '#' * 2 + ' ' * 5 + '#' * 2)
    print(' ' * 12 + '#' * 2 + ' ' * 3 + '#' * 2 + ' ' * 7 + '#' * 2 + ' ' * 3 + '#' * 2)
    print(' ' * 14 + '#' * 2 + ' ' * 12 + '#' * 2)
print('#'*200)
print('Welcome  to  this    绝无仅有的 聊天室  ')

class new_nomal_user:
    new_nomal_user_choice=input('是否需要引导您使用本聊天室(Y/N):')
    if new_nomal_user_choice=='Y':
        print("欢迎进入此引导界面.....................")
        leadr_new_normal_user='''
        不想引导你，直接跳到主页面把   
         ..................................................................................
        '''

        print(leadr_new_normal_user)
        from  nomal_user import  nomal_user_main
        nomal_user_main.normal_user_main()
    elif new_nomal_user_choice=='N':
        print('你真的不需要引导你使用本聊天室吗..................???????????')
        again_nomal_user=input('请输入(Y/N):')
        if again_nomal_user=='Y':
            print('好吧，请直接进入主界面把')
            import  time
            time.sleep(3)
            from  nomal_user import nomal_user_main
            nomal_user_main.normal_user_main()
        else:
            print('返回到此界面')
    else:
        print('输入错误，麻烦您重新输入，ok？')


