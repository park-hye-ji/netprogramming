
from socket import *

port = 3333
BUFSIZE=4096
sock=socket(AF_INET,SOCK_DGRAM)
sock.bind(('',port))
mbox={}


while True:
    data,addr=sock.recvfrom(BUFSIZE)
    data=data.decode()
    response=data.split()
    if(response[0]=="quit"):
        break
    num=int(response[1])
    
    if (response[0]=="send"):
        if num not in mbox:
            mbox[num] = []
        msg=' '.join(response[2:])
        mbox[num].append(msg)
        sock.sendto("OK".encode(),addr)
        
    elif(response[0]=="receive"):
        if num in mbox and mbox[num]:
                resp = mbox[num].pop(0)
                sock.sendto(resp.encode(),addr)
        else:
            sock.sendto("No messages".encode(),addr) 
sock.close()  