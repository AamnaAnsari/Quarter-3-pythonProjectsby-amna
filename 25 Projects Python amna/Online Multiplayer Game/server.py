import socket
import threading
import pickle

# Set up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen()

print("Server started. Waiting for connections...")

positions = [(50, 50), (300, 300)]

def handle_client(conn, player):
    conn.send(pickle.dumps(positions[player]))
    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            positions[player] = data
            if not data:
                break
            conn.send(pickle.dumps(positions))
        except:
            break

    conn.close()

player_count = 0
while True:
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    thread = threading.Thread(target=handle_client, args=(conn, player_count))
    thread.start()
    player_count += 1
