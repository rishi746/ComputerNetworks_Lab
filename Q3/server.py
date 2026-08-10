import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


data, addr = server_socket.recvfrom(1024)

number = int(data.decode())

if is_prime(number):
    result = "Prime number"
else:
    result = "Not a prime number"

server_socket.sendto(result.encode(), addr)

server_socket.close()