import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ',addr)
    client.send(b'hello ' + addr[0].encode())

    #학생 이름 수신 후 출력
    s_name=client.recv(1024)
    print(s_name.decode())

    #학생의 학번 전송
    s_id=20211494
    byte_id=s_id.to_bytes(10,'big')
    client.send(byte_id)
    client.close()