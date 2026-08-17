import math
import socket
import threading


HOST, PORT = "127.0.0.1", 5000


def handle(connection):
    with connection:
        reader = connection.makefile("r", encoding="utf-8")
        for value in reader:
            try:
                number = int(value)
                response = str(math.factorial(number)) if number >= 0 else "Invalid input"
            except ValueError:
                response = "Invalid input"
            connection.sendall(response.encode() + b"\n")


with socket.create_server((HOST, PORT)) as server:
    print(f"Factorial server listening on {HOST}:{PORT}")
    while True:
        connection, _ = server.accept()
        threading.Thread(target=handle, args=(connection,), daemon=True).start()