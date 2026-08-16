import socket
import threading
import sys

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(f"\n{message}\n> ", end="", flush=True)
        except:
            break
    sock.close()
    sys.exit()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))
    
    username = input("Enter username: ")
    client.send(username.encode())

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        try:
            msg = input("> ")
            client.send(msg.encode())
            if msg.lower() == '/quit':
                break
        except:
            break
    client.close()

if __name__ == "__main__":
    start_client()