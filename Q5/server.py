import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

filename = conn.recv(1024).decode()

try:
    file = open(filename, "r")

    content = file.read()

    lines = len(content.splitlines())
    words = len(content.split())
    characters = len(content)

    result = (
        "Lines: " + str(lines) +
        "\nWords: " + str(words) +
        "\nCharacters: " + str(characters)
    )

    file.close()

except FileNotFoundError:
    result = "File not found"

conn.send(result.encode())

conn.close()
server_socket.close()