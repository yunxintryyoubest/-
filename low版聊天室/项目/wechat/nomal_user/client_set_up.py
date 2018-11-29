############################################客户端启动环节############################################
import os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

class client_set_up:
    start_client=input('请输入run开启聊天室（client端）：')
    if start_client=='run':
        from  nomal_user import  client
        client.client_main()
