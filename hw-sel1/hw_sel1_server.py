import socket
import select
import time

def broadcast_data(clients, c_sock, message):
    for client_socket in clients:
        if client_socket != c_sock and client_socket != s_socket:
            try:
                client_socket.send(message)
            except Exception as e:
                print(f"Error {clients[client_socket]}: {e}")
                client_socket.close()
                del clients[client_socket]

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(('', 2500))
s_socket.listen()

print("Server started")

clients = {s_socket: "Server"}

try:
    while True:
        r_sock, w_sock, e_sock = select.select(clients.keys(), [], clients.keys())

        for event_sock in r_sock:
            if event_sock == s_socket:
                conn, addr = s_socket.accept()
                clients[conn] = addr
                print(f"New client connected: {addr}")
            else:
                data = event_sock.recv(1024)
                if not data or 'quit' in data.decode().lower() :
                    print(f"{clients[event_sock]} exited")
                    event_sock.close()
                    del clients[event_sock]
                else:
                    print(f"{time.asctime()} {clients[event_sock]}: {data.decode()}")
                    broadcast_data(clients, event_sock, data)

        for event_sock in e_sock:
            if event_sock in clients:
                del clients[event_sock]
                event_sock.close()

except KeyboardInterrupt:
    print("Server is shut down...")
finally:
    s_socket.close()
