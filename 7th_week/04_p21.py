import binascii
import socket
import sys

for string_address in ['114.71.220.95']:
    packed = socket.inet_aton(string_address)
    print('Original: ',string_address)
    byte_packed=binascii.hexlify(packed)
    print('Packed: ',byte_packed)
    print('size: ',sys.getsizeof((byte_packed)))
    print('Unpacked: ',socket.inet_ntoa(packed))
    print('size: ',sys.getsizeof((packed)))
    