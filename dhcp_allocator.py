import random

class DHCPAllocator:

    def __init__(self):
        self.pool = list(range(10000, 10025))
        self.assigned = {}

    def request(self, client_id):

        if not self.pool:
            return None

        port = self.pool.pop(0)
        self.assigned[client_id] = port
        return port

    def release(self, client_id):
        port = self.assigned.pop(client_id, None)
        if port:
            self.pool.append(port)
