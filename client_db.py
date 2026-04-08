import json
import os
import time

class ClientDB:
    def __init__(self, json_file='data/clients.json'):
        self.json_file = json_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                return json.load(f)
        return {'clients': [], 'metadata': {'created': self.current_time(), 'version': 1, 'last_updated': self.current_time()}}

    def save_data(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def register_client(self, client):
        self.data['clients'].append(client)
        self.data['metadata']['last_updated'] = self.current_time()
        self.save_data()

    def update_client(self, client_id, updates):
        for client in self.data['clients']:
            if client['id'] == client_id:
                client.update(updates)
                self.data['metadata']['last_updated'] = self.current_time()
                self.save_data()
                return

    def delete_client(self, client_id):
        self.data['clients'] = [c for c in self.data['clients'] if c['id'] != client_id]
        self.data['metadata']['last_updated'] = self.current_time()
        self.save_data()

    def get_client(self, client_id):
        for client in self.data['clients']:
            if client['id'] == client_id:
                return client
        return None

    def get_all_clients(self):
        return self.data['clients']

    def get_clients_by_sandbox(self, sandbox_id):
        return [client for client in self.data['clients'] if client.get('sandbox_id') == sandbox_id]

    def heartbeat(self, client_id):
        for client in self.data['clients']:
            if client['id'] == client_id:
                client['last_heartbeat'] = self.current_time()
                self.data['metadata']['last_updated'] = self.current_time()
                self.save_data()
                return

    def update_statistics(self, client_id, stats):
        for client in self.data['clients']:
            if client['id'] == client_id:
                client['statistics'] = stats
                self.data['metadata']['last_updated'] = self.current_time()
                self.save_data()
                return

    def get_stats(self, client_id):
        for client in self.data['clients']:
            if client['id'] == client_id:
                return client.get('statistics', {})
        return None

    def init_db(self):
        self.data = {'clients': [], 'metadata': {'created': self.current_time(), 'version': 1, 'last_updated': self.current_time()}}
        self.save_data()

    def current_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())