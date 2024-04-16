import socket

HOSTS =['www.sch.ac.kr','homepage.sch.ac.kr','www.naver.com','korea.net','www.mystic89.net']

for host in HOSTS:
    try:
        print('{} : {}'.format(host,socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host,msg))