import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

while True:
    print("\n1. Insert 2. Delete 3. Update 4. Search 5. Display 6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        sid, name, dept, sem, email = input("ID: "), input("Name: "), input("Dept: "), input("Sem: "), input("Email: ")
        client.sendall(f"INSERT|{sid}|{name}|{dept}|{sem}|{email}".encode())
    elif choice == '2':
        sid = input("ID: ")
        client.sendall(f"DELETE|{sid}".encode())
    elif choice == '3':
        sid, name, dept, sem, email = input("ID: "), input("New Name: "), input("New Dept: "), input("New Sem: "), input("New Email: ")
        client.sendall(f"UPDATE|{sid}|{name}|{dept}|{sem}|{email}".encode())
    elif choice == '4':
        sid = input("ID: ")
        client.sendall(f"SEARCH|{sid}".encode())
    elif choice == '5':
        client.sendall(b"DISPLAY")
    elif choice == '6':
        client.sendall(b"EXIT")
        break
    else:
        print("Invalid choice")
        continue
        
    print("Server Response:\n" + client.recv(4096).decode())
client.close()