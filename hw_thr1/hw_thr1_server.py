import socket
import threading
import time

def client_thread(conn, addr, clients):
    try:
        print(f"New client connected: {addr}")
        while True:
            data = conn.recv(1024)
            if not data or data.decode().lower() == 'quit':
                break
            print(f"{time.asctime()} {str(addr)}: {data.decode()}")
            for client_conn, client_addr in clients.items():
                if client_addr != addr:
                    client_conn.send(data)
    finally:
        print(f"{addr} exited")
        conn.close()
        del clients[conn]


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 2500))
server_socket.listen()

print("Server started, waiting for connections...")

clients = {}

try:
    while True:
        conn, addr = server_socket.accept()
        clients[conn] = addr
        threading.Thread(target=client_thread, args=(conn, addr, clients)).start()
except KeyboardInterrupt:
    print("Server is shutting down...")
finally:
    server_socket.close()

