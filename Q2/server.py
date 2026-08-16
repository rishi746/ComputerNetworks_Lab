import socket
import threading
import math

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode().strip()
        num = int(data)
        if num < 0:
            client_socket.send("Error: Factorial not defined for negative numbers.".encode())
        else:
            result = math.factorial(num)
            client_socket.send(f"Factorial of {num} = {result}".encode())
    except ValueError:
        client_socket.send("Error: Invalid input. Please enter an integer.".encode())
    except Exception:
        pass
    finally:
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client_socket, _ = server.accept()
    threading.Thread(target=handle_client, args=(client_socket,)).start()