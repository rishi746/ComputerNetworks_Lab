import socket
import hashlib
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

filepath = input("Enter file name: ")
if not os.path.exists(filepath):
    print("File not found.")
    client.close()
    exit()

filesize = os.path.getsize(filepath)
filename = os.path.basename(filepath)

sha256_hash = hashlib.sha256()
with open(filepath, "rb") as f:
    while chunk := f.read(4096):
        sha256_hash.update(chunk)
original_hash = sha256_hash.hexdigest()

client.send(f"{filename}|{filesize}|{original_hash}".encode())

if client.recv(1024) == b"READY":
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            client.sendall(chunk)

print("Server verification:\n" + client.recv(1024).decode())
client.close()