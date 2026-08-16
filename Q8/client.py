import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

username = input("Enter your name: ")
client.sendall(username.encode())

while True:
    data = client.recv(4096).decode()
    if not data:
        break
    if data == "INVALID":
        print("Invalid answer. Please enter A, B, C or D.")
        ans = input("Enter your answer: ")
        client.sendall(ans.encode())
        continue
    
    print(f"\n{data}")
    
    if "Final Score" in data:
        break
    
    if "Question" in data:
        ans = input("Enter your answer: ")
        client.sendall(ans.encode())

client.close()