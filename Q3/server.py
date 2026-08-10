import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

number = input("Enter a number: ")

client_socket.sendto(number.encode(), (HOST, PORT))

data, addr = client_socket.recvfrom(1024)

print("Server response:", data.decode())

client_socket.close()