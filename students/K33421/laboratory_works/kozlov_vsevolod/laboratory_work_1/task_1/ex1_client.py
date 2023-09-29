import socket

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.connect(('127.0.0.1', 14901))
    conn.send(b'Hello, server')
    msg_from_server = conn.recv(14000).decode('utf-8')
    print(msg_from_server)
    conn.close()


if __name__ == '__main__':
    main()