import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

numbers = input("Enter integers separated by spaces: ")

client_socket.send(numbers.encode())

result = client_socket.recv(1024).decode()

print("Sorted array:", result)

client_socket.close()