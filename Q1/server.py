import socket
import threading


HOST, PORT = "127.0.0.1", 5000
clients = {}
lock = threading.Lock()


def send_line(connection, message):
    connection.sendall(message.encode() + b"\n")


def broadcast(sender, message):
    with lock:
        recipients = [connection for connection in clients if connection is not sender]
    for connection in recipients:
        try:
            send_line(connection, message)
        except OSError:
            pass


def handle(connection):
    name = None
    try:
        reader = connection.makefile("r", encoding="utf-8")
        name = reader.readline().strip()
        with lock:
            if not name or name in clients.values():
                send_line(connection, "Username already taken")
                name = None
                return
            clients[connection] = name
        send_line(connection, "Username accepted")
        broadcast(connection, f"{name} joined the chat")
        for message in reader:
            broadcast(connection, f"{name}: {message.rstrip()}")
    except OSError:
        pass
    finally:
        with lock:
            clients.pop(connection, None)
        if name:
            broadcast(connection, f"{name} left the chat")
        connection.close()


with socket.create_server((HOST, PORT)) as server:
    print(f"Chat server listening on {HOST}:{PORT}")
    while True:
        connection, _ = server.accept()
        threading.Thread(target=handle, args=(connection,), daemon=True).start()