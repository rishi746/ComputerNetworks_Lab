import socket
import struct
import os

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2.0)
server_addr = ('127.0.0.1', 5000)

filename = input("Enter file name: ")
if not os.path.exists(filename):
    print("File not found.")
    exit()

seq = 1
header_format = "!I"

with open(filename, "rb") as f:
    while True:
        chunk = f.read(1024)
        is_eof = not chunk
        if is_eof:
            chunk = b"EOF"

        packet = struct.pack(header_format, seq) + chunk
        
        while True:
            client.sendto(packet, server_addr)
            try:
                ack_data, _ = client.recvfrom(1024)
                ack_seq = struct.unpack(header_format, ack_data)[0]
                if ack_seq == seq:
                    seq += 1
                    break
            except socket.timeout:
                print(f"Timeout occurred. Retransmitting SEQ={seq}")
        if is_eof:
            break