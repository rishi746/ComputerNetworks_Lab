import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = input("Enter a string: ")

client_socket.send(message.encode())

data = client_socket.recv(1024).decode()

print("Uppercase string:", data)

client_socket.close()