import json

class EmotionalState:
    def __init__(self):
        self.metrics = {
            'stress': 0.0,
            'confidence': 0.0,
            'curiosity': 0.0,
            'trust': 0.0,
            'urgency': 0.0
        }
        self.history = []

    def update_emotions(self, cluster_metrics):
        """Calculate emotions from cluster metrics"""
        self.metrics['stress'] = cluster_metrics.get('cpu_load', 0.0) * 0.7 + cluster_metrics.get('latency', 0.0) * 0.3
        self.metrics['confidence'] = 1 - cluster_metrics.get('failure_rate', 0.0)
        self.metrics['curiosity'] = cluster_metrics.get('novelty_score', 0.0)
        self.metrics['trust'] = cluster_metrics.get('trust_score', 0.8)
        self.metrics['urgency'] = cluster_metrics.get('queue_depth', 0.0) / 100.0
        self.history.append(self.metrics.copy())

    def get_emotions(self):
        return self.metrics

    def save_to_json(self, filepath='data/emotional_state.json'):
        with open(filepath, 'w') as f:
            json.dump({
                'current': self.metrics,
                'history': self.history
            }, f, indent=2)

    def load_from_json(self, filepath='data/emotional_state.json'):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                self.metrics = data['current']
                self.history = data['history']
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    emotions = EmotionalState()
    emotions.update_emotions({'cpu_load': 0.6, 'latency': 0.2, 'failure_rate': 0.05, 'novelty_score': 0.3, 'trust_score': 0.81, 'queue_depth': 45})
    print(emotions.get_emotions())
    emotions.save_to_json()