import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

while True:
    cmd = input("Enter command: ").strip()
    if not cmd:
        continue
    client.sendall(cmd.encode())
    if cmd == "exit":
        break
    print("Server output:\n" + client.recv(4096).decode())
client.close()