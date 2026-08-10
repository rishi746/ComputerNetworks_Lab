import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))

data, addr = server_socket.recvfrom(1024)

message = data.decode()

print("Message:", message)
print("Client IP:", addr[0])
print("Client Port:", addr[1])

server_socket.close()