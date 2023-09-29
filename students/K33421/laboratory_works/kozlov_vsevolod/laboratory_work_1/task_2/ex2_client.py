import socket
import pickle


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('127.0.0.1', 14900))

    height = int(input('Height:'))
    lower_base = int(input('Lower base:'))
    upper_base = int(input('Upper base:'))

    trap_data = (lower_base, upper_base, height)
    encoded_trap_data = pickle.dumps(trap_data)
    conn.send(encoded_trap_data)

    server_response_enc = conn.recv(12000)
    server_response_dec = server_response_enc.decode('utf-8')
    print(f'Trapezoid area: {server_response_dec}')


if __name__ == '__main__':
    main()