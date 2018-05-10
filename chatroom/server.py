from socket import * 
import sys
import os
from signal import *

def do_login(s,user,name,addr):
    msg = name + ' 进入聊天室'
    for c in user:
        s.sendto(msg.encode(),c)
    user.append(addr)
    return

def do_chat(s,user,tmp,addr):
    msg = tmp[1] + ' 说: ' + ' '.join(tmp[2:]) 
    for c in user:
        if c != addr:
            s.sendto(msg.encode(),c)
    return 

def do_quit(s,user,name,addr):
    msg = name + ' 退出聊天室'
    user.remove(addr)
    for c in user:
        s.sendto(msg.encode(),c)
    return 


def do_child(s):
    #存放用户的列表,内容为用户的addr
    user = []

    while True:
        msg,addr = s.recvfrom(2048)
        msg = msg.decode()
        tmp = msg.split(' ')
        #'L zhangsan'
        if tmp[0] == 'L':
            do_login(s,user,tmp[1],addr)
        #'B zhangsan 内容'
        elif tmp[0] == 'B':
            do_chat(s,user,tmp,addr)
        #'Q zhangsan'
        elif tmp[0] == 'Q':
            do_quit(s,user,tmp[1],addr)
    return


#处理服务器的具体事情
def do_parent(s,addr):   
    while True:
        msg = 'B 管理员 '
        print('管理员消息：',end = '')
        sys.stdout.flush()
        text = sys.stdin.readline()
        # 'B 管理员 text'
        msg = msg + text
        s.sendto(msg.encode(),addr)
    s.close()
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print('argv error')
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建数据报套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    #防止僵尸进程
    signal(SIGCHLD,SIG_IGN)

    #创建新进程
    pid = os.fork()

    if pid < 0:
        print('create process failed')
        return
    elif pid == 0:
        do_child(s)
    else:
        do_parent(s,ADDR)

if __name__ == '__main__':
    main()
