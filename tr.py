import socket

HOST = '192.168.85.42'
PORT = 53

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    command = input("Enter command: ")

    client.sendall(command.encode())

    if command.lower() == "exit":
        break

    data = client.recv(4096)
    print("Output:\n", data.decode())

client.close()