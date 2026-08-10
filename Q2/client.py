import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Waiting for client...")

conn, addr = server_socket.accept()

data = conn.recv(1024).decode()

result = data.upper()

conn.send(result.encode())

conn.close()
server_socket.close()