# algorithms/proof_of_stake.py
import sys
import time
import random
import json

class ProofOfStakeAlgorithm:
    def __init__(self, nodes, stakes, node_id):
        self.nodes = nodes
        self.stakes = stakes
        self.node_id = node_id
        self.coordinator = None
        self.message_count = 0
        self.start_time = None

    def select_leader(self):
        total_stake = sum(self.stakes.values())
        chosen = random.uniform(0, total_stake)
        cumulative = 0
        
        for node, stake in self.stakes.items():
            cumulative += stake
            if cumulative >= chosen:
                self.coordinator = node
                self.message_count += 1
                break

        print(f"Node {self.coordinator} is selected as the leader based on stake")

    def run(self):
        self.start_time = time.time()
        self.select_leader()
        end_time = time.time()
        self.store_metrics(end_time - self.start_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        metrics = {
            'node_id': self.node_id,
            'message_count': message_count,
            'convergence_time': convergence_time,
            'coordinator': self.coordinator
        }
        with open(f'metrics_pos_node_{self.node_id}.json', 'w') as file:
            json.dump(metrics, file, indent=4)
        print(f"Metrics saved for node {self.node_id}: {metrics}")

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    stakes = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    node_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    pos = ProofOfStakeAlgorithm(nodes, stakes, node_id)
    pos.run()
