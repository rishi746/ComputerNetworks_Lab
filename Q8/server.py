import socket
import threading

questions = [
    {"question": "Which protocol is connection-oriented?\nA. UDP\nB. TCP\nC. IP\nD. ARP", "answer": "B"},
    {"question": "Which device forwards packets between networks?\nA. Switch\nB. Hub\nC. Router\nD. Repeater", "answer": "C"}
]

scores = {}
score_lock = threading.Lock()

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode().strip()
        with score_lock:
            scores[username] = 0

        for i, q in enumerate(questions):
            client_socket.sendall(f"Question {i+1}:\n{q['question']}".encode())
            
            while True:
                answer = client_socket.recv(1024).decode().strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                client_socket.sendall(b"INVALID")

            if answer == q['answer']:
                with score_lock:
                    scores[username] += 1
                client_socket.sendall(f"Correct answer.\nCurrent Score: {scores[username]}".encode())
            else:
                client_socket.sendall(f"Incorrect answer.\nCurrent Score: {scores[username]}".encode())

        final_msg = f"Final Score: {scores[username]} / {len(questions)}"
        client_socket.sendall(final_msg.encode())
    except:
        pass
    finally:
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client, _ = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()