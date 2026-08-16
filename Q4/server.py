import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 5000))

expected_seq = 1
dropped_seq2 = False

with open("received_sample.txt", "wb") as f:
    while True:
        data, addr = server.recvfrom(4096)
        header_size = struct.calcsize("!I")
        seq = struct.unpack("!I", data[:header_size])[0]
        chunk = data[header_size:]

        if seq == 2 and not dropped_seq2:
            dropped_seq2 = True
            continue
            
        if seq == expected_seq:
            if chunk == b"EOF":
                server.sendto(struct.pack("!I", seq), addr)
                break
            f.write(chunk)
            expected_seq += 1

        server.sendto(struct.pack("!I", seq), addr)