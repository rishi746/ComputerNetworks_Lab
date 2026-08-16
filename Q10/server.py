import socket
import threading
import logging
import os

logging.basicConfig(filename='server_activity.log', level=logging.INFO, format='%(asctime)s | %(message)s')
users = {"Alice": "alice123", "Bob": "bob123", "Charlie": "charlie123"}
STORAGE_DIR = "server_files"
os.makedirs(STORAGE_DIR, exist_ok=True)

def handle_client(client):
    try:
        creds = client.recv(1024).decode().split('|')
        user, pwd = creds[0], creds[1]
        
        if user not in users or users[user] != pwd:
            client.sendall(b"REJECT")
            logging.info(f"{user} | LOGIN | FAILED")
            client.close()
            return
            
        client.sendall(b"ACCEPT")
        logging.info(f"{user} | LOGIN | SUCCESS")

        while True:
            req = client.recv(1024).decode()
            if not req or req == "EXIT":
                break
            
            parts = req.split('|')
            op = parts[0]
            
            if op == "UPLOAD":
                filename = os.path.basename(parts[1])
                filesize = int(parts[2])
                client.sendall(b"READY")
                
                received_bytes = 0
                filepath = os.path.join(STORAGE_DIR, filename)
                with open(filepath, "wb") as f:
                    while received_bytes < filesize:
                        chunk = client.recv(min(4096, filesize - received_bytes))
                        if not chunk: break
                        f.write(chunk)
                        received_bytes += len(chunk)
                logging.info(f"{user} | UPLOAD | {filename} | SUCCESS")
                client.sendall(b"Upload completed successfully.")
                
            elif op == "DOWNLOAD":
                filename = os.path.basename(parts[1])
                filepath = os.path.join(STORAGE_DIR, filename)
                
                if not os.path.exists(filepath):
                    client.sendall(b"ERROR|File not found.")
                    logging.info(f"{user} | DOWNLOAD | {filename} | FAILED")
                else:
                    filesize = os.path.getsize(filepath)
                    client.sendall(f"READY|{filesize}".encode())
                    if client.recv(1024) == b"GO":
                        with open(filepath, "rb") as f:
                            while chunk := f.read(4096):
                                client.sendall(chunk)
                        logging.info(f"{user} | DOWNLOAD | {filename} | SUCCESS")
    except:
        pass
    finally:
        client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client_socket, _ = server.accept()
    threading.Thread(target=handle_client, args=(client_socket,)).start()