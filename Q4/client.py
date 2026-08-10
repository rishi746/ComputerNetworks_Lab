import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

while True:

    message = input("Enter message: ")

    client_socket.send(message.encode())

    if message == "exit":
        break

    data = client_socket.recv(1024).decode()

    print("Server:", data)

client_socket.close()