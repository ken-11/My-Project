from socket import *
import sys 
import os 
from signal import * 

def do_child(s,addr,name):
    while True:
        text = input('发言：')
        #表示客户端要退出
        if text == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(),addr)
            os.kill(os.getppid(),SIGKILL)
            sys.exit(0)
        #表示正常聊天
        else:
            msg = 'B %s %s'%(name,text)
            s.sendto(msg.encode(),addr)
    return

def do_parent(s):
    while True:
        msg,addr = s.recvfrom(2048)
        print(msg.decode())

def main():
    if len(sys.argv) < 3:
        print('argv error')
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建数据报套接字
    s = socket(AF_INET,SOCK_DGRAM)

    name = input('请输入姓名：')
    msg = 'L ' + name

    s.sendto(msg.encode(),ADDR)

    signal(SIGCHLD,SIG_IGN)

    pid = os.fork()
    if pid < 0:
        print('faild to create process')
    elif pid == 0:
        do_child(s,ADDR,name)
    else:
        do_parent(s)

if __name__ == '__main__':
    main()