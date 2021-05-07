import socket
import os
import tqdm

HOST = '127.0.0.1'
PORT = 65432

SEPARATOR = "|||||"
BUFFER_SIZE = 4 * 1024

while True:
    file_path = input("Send file path:")
    if file_path.lower() == 'exit':
        break

    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    progress = tqdm.tqdm(range(file_size), f"sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'Client: Connecting to {HOST}:{PORT}')
        s.connect((HOST, PORT))
        print(f'Client: Connected')

        s.send(f'{file_name}{SEPARATOR}{file_size}'.encode())

        with open(file_path, "rb") as f:
            for _ in progress:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break

                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        print("done")