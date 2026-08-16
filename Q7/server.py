import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

socket_list = [server]

while True:
    readable, _, _ = select.select(socket_list, [], [])
    
    for sock in readable:
        if sock is server:
            client_socket, _ = server.accept()
            socket_list.append(client_socket)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    socket_list.remove(sock)
                    sock.close()
                else:
                    sock.sendall(b"Message received")
            except:
                socket_list.remove(sock)
                sock.close()