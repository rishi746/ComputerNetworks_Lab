import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

num = input("Enter an integer: ")
client.send(num.encode())

response = client.recv(1024).decode()
print("Server Response:\n" + response)

client.close()