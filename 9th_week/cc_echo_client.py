import socket 
BUFSIZE = 1024

s=socket.create_connection(('localhost',2500))

while True:
    msg=input("message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    if not data:
        break
    print("received message: %s"%data.decode())


s.close()