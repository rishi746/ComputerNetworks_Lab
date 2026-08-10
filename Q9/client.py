import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

sentence = input("Enter a sentence: ")

client_socket.send(sentence.encode())

result = client_socket.recv(1024).decode()

print(result)

client_socket.close()