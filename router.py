class SandboxRouter:

    def route_inbound(self, box, data):
        # 3 inbound ports
        inbound_port = hash(data) % 3
        print(f"inbound → box {box} port {inbound_port}")

    def route_outgoing(self, box, data):
        # 2 outgoing ports
        out = hash(data) % 2
        print(f"outgoing → service {out}")
