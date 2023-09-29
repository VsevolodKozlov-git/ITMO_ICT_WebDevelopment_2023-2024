import socket


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(('127.0.0.1', 14901))
    data, client_addr = conn.recvfrom(12000)
    decoded_data = data.decode('utf-8')
    print(decoded_data)
    conn.sendto(b"Hello, client", client_addr)
    conn.close()


if __name__ == '__main__':
    main()