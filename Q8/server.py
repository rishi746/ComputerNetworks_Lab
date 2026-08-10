import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

file = open("received_file.txt", "wb")

while True:

    data = conn.recv(1024)

    if not data:
        break

    file.write(data)

file.close()

print("File received successfully")

conn.close()
server_socket.close()