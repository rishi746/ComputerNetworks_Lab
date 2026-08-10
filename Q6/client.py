import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter message: ")

client_socket.sendto(message.encode(), (HOST, PORT))

print("Message sent")

client_socket.close()