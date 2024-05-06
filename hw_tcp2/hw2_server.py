from socket import *

s=socket(AF_INET,SOCK_STREAM)
s.bind(('',3333))
s.listen(5)
print('waiting...')

while True:
    client, addr =s.accept()
    print('connection from ',addr)
    while True:
        data =client.recv(1024)
        if not data:
            break
        data=data.decode()
        res=0
        try:
            data = data.replace(" ", "")
            
            if '+' in data:
                numbers = data.split('+')
                res = int(numbers[0]) + int(numbers[1])
            elif '-' in data:
                numbers = data.split('-')
                res = int(numbers[0]) - int(numbers[1])
            elif '*' in data:
                numbers = data.split('*')
                res = int(numbers[0]) * int(numbers[1])
            elif '/' in data:
                numbers = data.split('/')
                res = int(numbers[0]) / int(numbers[1])
                res = format(res, ".1f")
        except:
            client.send(b'Try agin')
        else:
            client.send(str(res).encode())

    client.close()