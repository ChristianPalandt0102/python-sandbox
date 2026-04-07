import json
import random

class DreamEngine:
    def __init__(self, curiosity_threshold=0.5):
        self.curiosity_threshold = curiosity_threshold
        self.dreams = []

    def dream(self):
        idea = f"Idea {random.randint(1, 100)} for exploration"
        self.dreams.append(idea)
        return idea

    def mutate(self, idea):
        mutated_idea = idea + " (mutated)"
        return mutated_idea

    def imagine_world(self):
        world_state = f"World state {random.randint(1, 10)}"
        return world_state

    def value_world(self, world_state):
        value = random.uniform(0, 1)
        return value

    def should_explore(self, value):
        return value > self.curiosity_threshold

    def dream_cycle(self):
        idea = self.dream()
        mutated_idea = self.mutate(idea)
        world_state = self.imagine_world()
        value = self.value_world(world_state)

        if self.should_explore(value):
            return f'Exploring: {mutated_idea} in {world_state} with value {value}'
        return 'Not worth exploring'

    def dream_loop(self):
        results = []
        for _ in range(10):  # Simulate 10 cycles
            results.append(self.dream_cycle())
        return results

    def save_dreams(self, filename='dreams.json'):
        with open(filename, 'w') as f:
            json.dump(self.dreams, f)
