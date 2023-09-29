import socket
import concurrent.futures
import threading

stop_event = threading.Event()


def input_thread(conn: socket.socket):
    """Поток для ввода данных"""
    while not stop_event.is_set():
        msg = input()
        msg_encoded = msg.encode()
        conn.send(msg_encoded)
        if msg == 'Bye!':
            print('Stopped everything')
            stop_event.set()


def msg_printer_thread(conn: socket.socket):
    """Поток для вывода данных"""
    while not stop_event.is_set():
        msg = conn.recv(13000)
        print(msg.decode('utf-8'))


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('127.0.0.1', 14900))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(input_thread, conn)
        executor.submit(msg_printer_thread, conn)
    conn.close()


if __name__ == '__main__':
    main()