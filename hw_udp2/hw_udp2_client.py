
from socket import *
import random
import time

BUFF_SIZE=1024
port=3333

c_sock=socket(AF_INET,SOCK_DGRAM)
c_sock.connect(('localhost',port))



while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(),('localhost',port))
        c_sock.settimeout(2)
        try:
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    c_sock.settimeout(None)
    while True:
        data, addr = c_sock.recvfrom(BUFF_SIZE)       
        if random.random() <= 0.5:
            continue
        else:
            c_sock.sendto(b'ack', addr)
            if data.decode() =="ack":
                data=c_sock.recv(BUFF_SIZE)
            print('<-', data.decode())
            break
