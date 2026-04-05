from process_pool import spawn_port_workers

BOXES = 20
PORTS_PER_BOX = 5

class SandboxController:

    def __init__(self):
        self.boxes = {}

    def build(self):
        for box_id in range(BOXES):

            ports = []

            for port in range(PORTS_PER_BOX):
                workers = spawn_port_workers(box_id, port)
                ports.append(workers)

            self.boxes[box_id] = ports

        print("[SANDBOX] 20 boxes created")
