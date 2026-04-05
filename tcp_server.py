import socket
import threading

HOST = "0.0.0.0"
BASE_PORT = 9000

class TCPServer:

    def __init__(self, handler):
        self.handler = handler

    def start(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, port))
        s.listen()

        print(f"[TCP] listening {port}")

        while True:
            conn, addr = s.accept()
            threading.Thread(
                target=self.handler,
                args=(conn, addr),
                daemon=True
            ).start()
