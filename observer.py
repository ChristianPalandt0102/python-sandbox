import psutil
import json
import datetime

class SystemMetrics:
    def __init__(self):
        self.metrics_history = []

    def collect_metrics(self):
        cpu_load = psutil.cpu_percent(interval=1)
        memory_load = psutil.virtual_memory().percent
        disk_load = psutil.disk_usage('/').percent
        network_load = psutil.net_io_counters()
        processes = len(psutil.pids())
        load_state = self.evaluate_load(cpu_load, memory_load, disk_load)
        metrics = {
            'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'cpu_load': cpu_load,
            'memory_load': memory_load,
            'disk_load': disk_load,
            'processes': processes,
            'network_load': {
                'bytes_sent': network_load.bytes_sent,
                'bytes_recv': network_load.bytes_recv
            },
            'load_state': load_state
        }
        self.metrics_history.append(metrics)

    def evaluate_load(self, cpu, memory, disk):
        avg_load = (cpu + memory + disk) / 3
        if avg_load >= 80:
            return 'CRITICAL'
        elif avg_load >= 60:
            return 'HIGH'
        elif avg_load >= 40:
            return 'MEDIUM'
        else:
            return 'LOW'

    def save_metrics_to_json(self, filename='metrics_history.json'):
        with open(filename, 'w') as json_file:
            json.dump(self.metrics_history, json_file, indent=4)

if __name__ == '__main__':
    metrics_collector = SystemMetrics()
    for _ in range(10):  # Collect metrics 10 times for testing
        metrics_collector.collect_metrics()
    metrics_collector.save_metrics_to_json()  
