import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()

sentence = conn.recv(1024).decode()

vowels = 0
consonants = 0

for ch in sentence.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1

        else:
            consonants += 1

words = len(sentence.split())

result = (
    "Vowels: " + str(vowels) +
    "\nConsonants: " + str(consonants) +
    "\nWords: " + str(words)
)

conn.send(result.encode())

conn.close()
server_socket.close()