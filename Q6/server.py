import socket
import sqlite3

def setup_db():
    conn = sqlite3.connect("students.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            semester INTEGER,
            email TEXT
        )
    """)
    conn.commit()
    return conn, cursor

conn, cursor = setup_db()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

while True:
    client, _ = server.accept()
    while True:
        try:
            req = client.recv(1024).decode().strip()
            if not req or req == "EXIT": break
            parts = req.split('|')
            op = parts[0]
            
            if op == "INSERT":
                cursor.execute("SELECT * FROM students WHERE student_id = ?", (parts[1],))
                if cursor.fetchone():
                    client.sendall(f"Error: Student ID {parts[1]} already exists.".encode())
                else:
                    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", 
                                   (int(parts[1]), parts[2], parts[3], int(parts[4]), parts[5]))
                    conn.commit()
                    client.sendall(b"Record inserted successfully.")
                    
            elif op == "SEARCH":
                cursor.execute("SELECT * FROM students WHERE student_id = ?", (parts[1],))
                row = cursor.fetchone()
                if row:
                    client.sendall(f"ID: {row[0]}\nName: {row[1]}\nDepartment: {row[2]}\nSemester: {row[3]}\nEmail: {row[4]}".encode())
                else:
                    client.sendall(b"Student record not found.")
                    
            elif op == "UPDATE":
                cursor.execute("SELECT * FROM students WHERE student_id = ?", (parts[1],))
                if not cursor.fetchone():
                    client.sendall(b"No record found. Update not performed.")
                else:
                    cursor.execute("UPDATE students SET name=?, department=?, semester=?, email=? WHERE student_id=?", 
                                   (parts[2], parts[3], int(parts[4]), parts[5], int(parts[1])))
                    conn.commit()
                    client.sendall(b"Record updated successfully.")
                    
            elif op == "DELETE":
                cursor.execute("SELECT * FROM students WHERE student_id = ?", (parts[1],))
                if not cursor.fetchone():
                    client.sendall(b"No record found. Delete not performed.")
                else:
                    cursor.execute("DELETE FROM students WHERE student_id = ?", (parts[1],))
                    conn.commit()
                    client.sendall(b"Record deleted successfully.")
                    
            elif op == "DISPLAY":
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
                if not rows:
                    client.sendall(b"No records found.")
                else:
                    res = "\n".join([f"ID: {r[0]}, Name: {r[1]}, Dept: {r[2]}, Sem: {r[3]}, Email: {r[4]}" for r in rows])
                    client.sendall(res.encode())
        except Exception as e:
            client.sendall(f"Error processing request: {str(e)}".encode())
    client.close()