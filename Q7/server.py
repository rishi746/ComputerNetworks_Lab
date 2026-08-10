import socket

HOST = "127.0.0.1"
PORT = 5000


def is_palindrome(text):
    reversed_text = ""

    for ch in text:
        reversed_text = ch + reversed_text

    if text == reversed_text:
        return True
    else:
        return False


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Waiting for client...")

conn, addr = server_socket.accept()

text = conn.recv(1024).decode()

if is_palindrome(text):
    result = "Palindrome"
else:
    result = "Not a palindrome"

conn.send(result.encode())

conn.close()
server_socket.close()