import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

user = input("Username: ")
pwd = input("Password: ")
client.sendall(f"{user}|{pwd}".encode())

if client.recv(1024) == b"REJECT":
    print("Authentication failed.")
    client.close()
    exit()

print("Authentication successful.")

while True:
    print("\n1. Upload File\n2. Download File\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        filepath = input("Enter filename: ")
        if not os.path.exists(filepath):
            print("File not found.")
            continue
            
        filesize = os.path.getsize(filepath)
        filename = os.path.basename(filepath)
        client.sendall(f"UPLOAD|{filename}|{filesize}".encode())
        
        if client.recv(1024) == b"READY":
            with open(filepath, "rb") as f:
                while chunk := f.read(4096):
                    client.sendall(chunk)
            print(client.recv(1024).decode())
            
    elif choice == '2':
        filename = input("Enter filename: ")
        client.sendall(f"DOWNLOAD|{filename}".encode())
        
        resp = client.recv(1024).decode().split('|')
        if resp[0] == "ERROR":
            print(resp[1])
        elif resp[0] == "READY":
            filesize = int(resp[1])
            client.sendall(b"GO")
            received_bytes = 0
            with open("received_" + filename, "wb") as f:
                while received_bytes < filesize:
                    chunk = client.recv(min(4096, filesize - received_bytes))
                    f.write(chunk)
                    received_bytes += len(chunk)
            print("Download completed successfully.")
            
    elif choice == '3':
        client.sendall(b"EXIT")
        break

client.close()