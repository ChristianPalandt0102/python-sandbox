from sandbox_controller import SandboxController
from tcp_server import TCPServer
from web_builder import build
from client_db import init_db

def handler(conn, addr):
    data = conn.recv(1024)
    conn.send(b"ok")
    conn.close()

if __name__ == "__main__":

    init_db()
    build()

    controller = SandboxController()
    controller.build()

    TCPServer(handler).start(9000)
