import socket
import hashlib
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

client_socket, _ = server.accept()

metadata = client_socket.recv(1024).decode().split('|')
filename = os.path.basename(metadata[0])
filesize = int(metadata[1])
original_hash = metadata[2]

client_socket.send(b"READY")

sha256_hash = hashlib.sha256()
received_bytes = 0

with open("received_" + filename, "wb") as f:
    while received_bytes < filesize:
        chunk = client_socket.recv(min(4096, filesize - received_bytes))
        if not chunk:
            break
        f.write(chunk)
        sha256_hash.update(chunk)
        received_bytes += len(chunk)

calculated_hash = sha256_hash.hexdigest()

if calculated_hash == original_hash:
    client_socket.send(b"SHA-256 verification successful. File integrity verified.")
else:
    client_socket.send(b"FILE INTEGRITY CHECK FAILED")

client_socket.close()
server.close()