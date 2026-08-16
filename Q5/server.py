import socket
import os
from datetime import datetime

def handle_calculator(parts):
    try:
        a, b, op = float(parts[1]), float(parts[2]), parts[3]
        if op == '+': return str(a + b)
        elif op == '-': return str(a - b)
        elif op == '*': return str(a * b)
        elif op == '/': return str(a / b) if b != 0 else "Error - division by zero is not allowed."
        return "Invalid operator."
    except:
        return "Invalid numeric input."

def handle_string(parts):
    try:
        text, op = parts[1], parts[2].lower()
        if op == 'upper': return text.upper()
        elif op == 'lower': return text.lower()
        elif op == 'reverse': return text[::-1]
        return "Invalid string operation."
    except:
        return "Invalid string request."

def handle_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def handle_file(client_socket, filename):
    if not os.path.exists(filename):
        client_socket.sendall(b"ERROR|File not found.")
        return
    filesize = os.path.getsize(filename)
    client_socket.sendall(f"READY|{filesize}".encode())
    
    if client_socket.recv(1024).decode() == "GO":
        with open(filename, "rb") as f:
            while chunk := f.read(4096):
                client_socket.sendall(chunk)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client, _ = server.accept()
    while True:
        try:
            req = client.recv(1024).decode().strip()
            if not req or req == "EXIT":
                break
            parts = req.split('|')
            service = parts[0]
            
            if service == "CALC":
                client.sendall(handle_calculator(parts).encode())
            elif service == "STRING":
                client.sendall(handle_string(parts).encode())
            elif service == "TIME":
                client.sendall(handle_time().encode())
            elif service == "FILE":
                handle_file(client, os.path.basename(parts[1]))
            else:
                client.sendall(b"Invalid service selection.")
        except:
            break
    client.close()