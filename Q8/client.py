import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

filename = input("Enter filename: ")

file = open(filename, "rb")

while True:

    data = file.read(1024)

    if not data:
        break

    client_socket.send(data)

file.close()

client_socket.close()

print("File sent successfully")