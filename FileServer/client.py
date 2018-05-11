from socket import * 
import sys 
from time import sleep

class FtpClient(object):
    def __init__(self,serveraddr):
        self.serveraddr = serveraddr

    def do_list(self):
        tcp_sock = socket()
        tcp_sock.connect(self.serveraddr)
        tcp_sock.send('L'.encode())

        data = tcp_sock.recv(1024).decode()
        if data == 'OK':
            while True:
                data = tcp_sock.recv(1024).decode()
                if data == '##':
                    break
                print(data)
            print('List OK!')
            tcp_sock.close()
            return
        else:
            print('List error!')
            tcp_sock.close()
            return

    def do_get(self,filename):
        fd = open(filename,'w')
        data = 'G ' + filename
        tcp_sock = socket()
        tcp_sock.connect(self.serveraddr)
        tcp_sock.send(data.encode())

        data = tcp_sock.recv(1024).decode()
        if data == 'OK':
            while True:
                data = tcp_sock.recv(1024).decode()
                if data == '##':
                    break
                fd.write(data)
            fd.close()
            print('get file OK!')
            tcp_sock.close()
            return
        else:
            print('get file error!')
            tcp_sock.close()
            return

    def do_put(self,filename):
        fd = open(filename,'rb')
        data = 'P ' + filename 

        tcp_sock = socket()
        tcp_sock.connect(self.serveraddr)
        tcp_sock.send(data.encode())
        data = tcp_sock.recv(1024).decode()
        if data == 'OK':
            for line in fd:
                tcp_sock.send(line)
            sleep(0.1)
            tcp_sock.send('##'.encode())
            fd.close()
            tcp_sock.close()
            print('put %s ok!'%filename)
            return   
        else:
            print('put %s fail!'%filename)
            fd.close()
            tcp_sock.close()
            return


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    BUFFERSIZE = 1024
    ADDR = (HOST,PORT)

    while True:
        print('*******command*********')
        print('*******  list  ********')
        print('******get filename*****')
        print('******put filename*****')
        print('*******  quit  ********') 
        data = input('Input command>>')

        ftp = FtpClient(ADDR)

        if data[:4] == 'list':
            ftp.do_list()
        elif data[:3] == 'get':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[:3] == 'put':
            filename = data.split(' ')[-1]
            ftp.do_put(filename) 
        elif data == 'quit':
            sys.exit(0)
        else:
            print('请重新输入！')
            continue



if __name__ == '__main__':
    main()