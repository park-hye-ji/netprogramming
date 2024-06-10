import socket
import threading

def hadnler(sock):
    while True:
        msg=sock.recv(1024)
        if not msg:
            break
        print(msg.decode())


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',2500))

my_id=input('ID를 입력하시오.: ')
sock.send(('['+my_id+']').encode())

th=threading.Thread(target=hadnler,args=(sock,))
th.daemon=True
th.start()

while True:
    msg='['+my_id+'] '+input()
    sock.send(msg.encode())