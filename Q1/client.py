import socket
import threading


HOST, PORT = "127.0.0.1", 5000


with socket.create_connection((HOST, PORT)) as client:
    client.sendall(input("Name: ").encode() + b"\n")
    reader = client.makefile("r", encoding="utf-8")
    status = reader.readline().strip()
    print(status)
    if status != "Username accepted":
        raise SystemExit(1)

    def receive():
        for message in reader:
            print(message, end="")

    threading.Thread(target=receive, daemon=True).start()
    try:
        while True:
            client.sendall(input().encode() + b"\n")
    except (EOFError, KeyboardInterrupt):
        pass