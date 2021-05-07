import socket
import os
import tqdm

HOST = '0.0.0.0' 
PORT = 65432 

SEPARATOR = "|||||"
BUFFER_SIZE = 4 * 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Start to listen on port {PORT}')
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            recv = conn.recv(BUFFER_SIZE).decode()
            filename, filesize = recv.split(SEPARATOR)
            filesize = int(filesize)

            progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(filename, "wb") as f:
                for _ in progress:
                    bytes_read = conn.recv(BUFFER_SIZE)
                    if not bytes_read:    
                        break
                    f.write(bytes_read)
                    progress.update(len(bytes_read))
            print("done")
    