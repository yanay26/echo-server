import socket

# ЗАДАНИЕ 3: Напишите простой TCP-клиент, который устанавливает соединение с сервером,
# считывает строку со стандартного ввода и посылает его серверу.
def echo_client(host, port):
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Устанавливаем соединение с сервером
    client_socket.connect((host, port))
    print(f"Установлено соединение с сервером {host}:{port}")

    try:
        # Считываем строку со стандартного ввода
        message = input("Введите строку для отправки серверу: ")
        # Отправляем сообщение серверу
        client_socket.sendall(message.encode())
        print("Отправка данных серверу")

        # Принимаем ответ от сервера
        data = client_socket.recv(1024)
        print("Прием данных от сервера:", data.decode())
    finally:
        # Закрываем соединение с сервером
        client_socket.close()

# ЗАДАНИЕ 4: Добавить вывод служебных сообщений при наступлении различных событий для клиента.
def connect_to_server(host, port):
    print(f"Соединение с сервером {host}:{port}")

def disconnect_from_server():
    print("Разрыв соединения с сервером")

def send_data_to_server():
    print("Отправка данных серверу")

def receive_data_from_server():
    print("Прием данных от сервера")


if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 12345  # Произвольный порт

    connect_to_server(HOST, PORT)
    echo_client(HOST, PORT)
    disconnect_from_server()
