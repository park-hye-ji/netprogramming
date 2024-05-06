from socket import *

s=socket(AF_INET,SOCK_STREAM)

s.connect(('localhost',3333))

while True:
    msg =input('계산 할 식을 입력하시오.(가능 연산: 덧셈, 뺄셈, 곱셈, 나눗셈): ')
    if msg=='q':
        break
    s.send(msg.encode())

    print('Result is: ',s.recv(1024).decode())
s.close()