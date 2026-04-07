import json
import logging
from queue import Queue
import threading

# Setup logging to JSON file
logging.basicConfig(filename='event_log.json', level=logging.INFO, format='%(asctime)s - %(message)s')

class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.event_queue = Queue()
        self.is_running = True
        self.listener_thread = threading.Thread(target=self.process_events)
        self.listener_thread.start()

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def publish(self, event_type, data):
        self.event_queue.put((event_type, data))
        logging.info(f'Published event: {event_type} with data: {data}')

    def process_events(self):
        while self.is_running:
            try:
                event_type, data = self.event_queue.get(timeout=1)
                self.handle_event(event_type, data)
            except Exception as e:
                logging.error(f'Error processing event: {e}')  

    def handle_event(self, event_type, data):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)
                logging.info(f'Handled event: {event_type} with data: {data}')

    def stop(self):
        self.is_running = False
        self.listener_thread.join()

# Example usage
if __name__ == '__main__':
    bus = EventBus()

    def handle_failure(data):
        print(f'Handling failure: {data}')

    def handle_update(data):
        print(f'Handling update: {data}')

    # Subscribing to events
    bus.subscribe('sandbox_failure', handle_failure)
    bus.subscribe('learning_update', handle_update)

    # Publishing events
    bus.publish('sandbox_failure', {'reason': 'Out of Memory'})
    bus.publish('learning_update', {'accuracy': 0.95})
