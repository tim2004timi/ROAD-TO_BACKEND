import socket

# domain:5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server_socket.bind(("localhost", 5000))
server_socket.listen()

while True:
    print("Before .accept()")
    client_socket, addr = server_socket.accept()
    print("Connect from", addr)

    while True:
        print("Before .recv()")
        request = client_socket.recv(1024)

        if not request:
            break
        else:
            response = "Hello world\n".encode()
            client_socket.send(response)
