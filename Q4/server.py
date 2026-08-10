import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

while True:

    data = conn.recv(1024).decode()

    if data == "exit":
        break

    print("Received:", data)

    conn.send(data.encode())

conn.close()
server_socket.close()