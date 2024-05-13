from socket import *

s=socket()
s.bind(('',80))
s.listen(10)

while True:
    c,addr = s.accept()

    data=c.recv(1024)
    if not data:
        break
    msg=data.decode()
    req=msg.split('\r\n')

    req_1=req[0].split()
    filename = req_1[1].replace("/", "")
    

    if (filename=='index.html'):
        f=open(filename,'r',encoding='utf-8')
        mimeType='text/html'
    elif (filename=='iot.png'):
        f=open(filename,'rb')
        mimeType='image/png'
    elif (filename=='favicon.ico'):
        f=open(filename,'rb')
        mimeType='image/x-icon'
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
        c.close()
        continue

    filedata=f.read()
    
    c.send(b'HTTP/1.1 200 OK\r\n')
    c.send(b'Content-Type: '+mimeType.encode()+b'\r\n')
    c.send(b'\r\n')
    if (filename=='index.html'):
        c.send(filedata.encode('utf-8'))
    else:
        c.send(filedata)

    c.close()


