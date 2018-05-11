from socket import *
import sys
import os
from time import sleep


class FtpServer(object):
    def __init__(self, client_sock):
        self.client_sock = client_sock

    def do_list(self):
        filelist = os.listdir('.')#获取当前路径下所有文件名
        if filelist == None:
            self.client_sock.send('FALL'.encode())
        self.client_sock.send('OK'.encode())
        sleep(0.1)
        for filename in filelist:
            #判断当前文件，隐藏文件和文件夹筛选出来
            if filename[0] != '.' and os.path.isfile(filename):            
                self.client_sock.send(filename.encode())
            sleep(0.1)
        self.client_sock.send('##'.encode())
        print('send file list ok')
        return

    def do_get(self, filename):
        try:
            fd = open(filename, 'rb')
        except:
            self.client_sock.send('FALL'.encode())

        self.client_sock.send('OK'.encode())
        sleep(0.1)
        for line in fd:
            self.client_sock.send(line)
        fd.close()
        sleep(0.1)
        self.client_sock.send('##'.encode())
        print('send file ok')
        return

    def do_put(self, filename):
        try:
            fd = open(filename, 'w')
        except:
            self.client_sock.send('FALL'.encode())
        self.client_sock.send('OK'.encode())
        sleep(0.1)
        while True:
            data = self.client_sock.recv(1024).decode()
            if data == '##':
                break
            fd.write(data)
        fd.close()
        print('put file ok!')
        return


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    BUFFERSIZE = 1024
    ADDR = (HOST, PORT)

    # tcp的方式创建套接字
    tcp_sock = socket()
    tcp_sock.bind(ADDR)
    tcp_sock.listen(5)
    while True:
        client_sock, addr = tcp_sock.accept()
        print('Connect from', addr)
        # 接收具体需要什么请求
        data = client_sock.recv(BUFFERSIZE).decode()
        ftp = FtpServer(client_sock)

        if data[0] == 'L':
            ftp.do_list()
        if data[0] == 'G':
            ftp.do_get(data[2:])
        if data[0] == 'P':
            ftp.do_put(data[2:])


if __name__ == '__main__':
    main()
