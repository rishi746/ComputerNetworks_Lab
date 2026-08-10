import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

data = conn.recv(1024).decode()

numbers = list(map(int, data.split()))

numbers.sort()

result = " ".join(map(str, numbers))

conn.send(result.encode())

conn.close()
server_socket.close()