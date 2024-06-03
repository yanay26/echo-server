import socket

# ЗАДАНИЕ 1: Создать простой TCP-сервер, который принимает от клиента строку (порциями по 1 КБ) и возвращает ее (эхо-сервер).
def echo_server(host, port):
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к указанному хосту и порту
    server_socket.bind((host, port))
    # Начинаем прослушивать входящие соединения
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        # Принимаем входящее соединение
        client_socket, client_address = server_socket.accept()
        print(f"Получено входящее соединение от {client_address}")

        # Принимаем данные от клиента и отправляем их обратно
        while True:
            data = client_socket.recv(1024)  # Принимаем данные (порциями по 1 КБ)
            if not data:
                break  # Если данные не получены, выходим из цикла
            client_socket.sendall(data)  # Отправляем данные обратно клиенту

        # Закрываем соединение с клиентом
        client_socket.close()

# ЗАДАНИЕ 2: Добавить вывод служебных сообщений при наступлении различных событий для сервера.
def start_server():
    print("Запуск сервера")

def listen_port(host, port):
    print(f"Начало прослушивания порта {host}:{port}")

def client_connection(client_address):
    print(f"Подключение клиента {client_address}")

def receive_data():
    print("Прием данных от клиента")

def send_data():
    print("Отправка данных клиенту")

def disconnect_client():
    print("Отключение клиента")

def stop_server():
    print("Остановка сервера")

if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 12345  # Произвольный порт

    start_server()
    listen_port(HOST, PORT)
    echo_server(HOST, PORT)
