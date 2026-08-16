import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

while True:
    msg = input("Enter message: ")
    if msg.lower() == "exit":
        break
    client.sendall(msg.encode())
    print("Server:", client.recv(1024).decode())
client.close()