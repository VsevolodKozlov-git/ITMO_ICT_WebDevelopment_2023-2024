import socket
import pickle


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind(('127.0.0.1', 14900))
    conn.listen(10)

    client_socket, address = conn.accept()
    encoded_data = client_socket.recv(12000)
    lower_base, upper_base, height = pickle.loads(encoded_data)

    area = (upper_base + lower_base) / 2 * height
    area = round(area, 2)

    area_encoded = str(area).encode('utf-8')
    client_socket.send(area_encoded)
    conn.close()


if __name__ == '__main__':
    main()