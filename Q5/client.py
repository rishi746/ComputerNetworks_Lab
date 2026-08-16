import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

while True:
    print("\n1. Calculator\n2. String Operations\n3. File Transfer\n4. Time Service\n5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        a, b, op = input("Enter first number: "), input("Enter second number: "), input("Enter operator (+, -, *, /): ")
        client.sendall(f"CALC|{a}|{b}|{op}".encode())
        print("Server Result:", client.recv(1024).decode())
        
    elif choice == '2':
        txt, op = input("Enter string: "), input("Enter operation (upper/lower/reverse): ")
        client.sendall(f"STRING|{txt}|{op}".encode())
        print("Server Result:", client.recv(1024).decode())
        
    elif choice == '4':
        client.sendall(b"TIME")
        print("Server Time:", client.recv(1024).decode())
        
    elif choice == '3':
        filename = input("Enter filename: ")
        client.sendall(f"FILE|{filename}".encode())
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
            print("File received successfully.")
            
    elif choice == '5':
        client.sendall(b"EXIT")
        break
    else:
        print("Invalid choice.")
client.close()