import socket


HOST, PORT = "127.0.0.1", 5000


with socket.create_connection((HOST, PORT)) as client:
    reader = client.makefile("r", encoding="utf-8")
    while (value := input("Enter a non-negative integer (blank to quit): ")):
        client.sendall(value.encode() + b"\n")
        print("Factorial:", reader.readline().strip())