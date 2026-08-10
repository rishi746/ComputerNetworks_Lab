import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

data = conn.recv(1024).decode()

a, operator, b = data.split()

a = float(a)
b = float(b)

if operator == "+":
    result = a + b

elif operator == "-":
    result = a - b

elif operator == "*":
    result = a * b

elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operator"

conn.send(str(result).encode())

conn.close()
server_socket.close()