import socket
import threading

clients = {}
clients_lock = threading.Lock()

def broadcast(message, sender_socket):
    with clients_lock:
        for client_socket in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode())
                except:
                    pass

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode().strip()
        with clients_lock:
            if username in clients.values():
                client_socket.send("Error: Username already taken.".encode())
                client_socket.close()
                return
            clients[client_socket] = username
        
        client_socket.send(f"Welcome, {username}!".encode())
        broadcast(f"[{username}] has joined the chat.", client_socket)

        while True:
            msg = client_socket.recv(1024).decode()
            if not msg or msg.lower() == '/quit':
                break
            broadcast(f"[{username}] {msg}", client_socket)
    except:
        pass
    finally:
        with clients_lock:
            if client_socket in clients:
                username = clients[client_socket]
                del clients[client_socket]
                broadcast(f"[{username}] has left the chat.", None)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen()
    while True:
        client_socket, _ = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()