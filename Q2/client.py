import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

a = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /): ")
b = input("Enter second number: ")

message = a + " " + operator + " " + b

client_socket.send(message.encode())

result = client_socket.recv(1024).decode()

print("Result:", result)

client_socket.close()