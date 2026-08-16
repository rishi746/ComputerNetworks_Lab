import socket
import subprocess

allowed_commands = {
    "pwd": ["pwd"],
    "ls": ["ls"],
    "date": ["date"]
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client, _ = server.accept()
    while True:
        try:
            cmd = client.recv(1024).decode().strip()
            if not cmd:
                client.sendall(b"Error: Empty command.")
                continue
            if cmd == "exit":
                break

            if cmd in allowed_commands:
                try:
                    result = subprocess.run(allowed_commands[cmd], capture_output=True, text=True, timeout=5)
                    output = result.stdout if result.returncode == 0 else result.stderr
                    client.sendall(output.encode() if output else b"Command executed successfully.")
                except subprocess.TimeoutExpired:
                    client.sendall(b"Error: Command execution timed out.")
                except Exception as e:
                    client.sendall(f"Error during execution: {str(e)}".encode())
            else:
                client.sendall(b"Error: Command not permitted. Allowed commands: pwd, ls, date")
        except:
            break
    client.close()