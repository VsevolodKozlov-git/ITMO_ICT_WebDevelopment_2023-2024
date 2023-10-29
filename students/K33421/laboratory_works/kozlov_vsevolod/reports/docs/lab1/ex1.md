# Упраженение 1

## Код 

### Клиента

```python
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
```

### Сервера

```python
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
```

## Демонстрация работы

![Сервер](img/ex1_server.PNG)

*Вывод сервера*

---
![client](img/ex1_client.png)

*Вывод клиента*