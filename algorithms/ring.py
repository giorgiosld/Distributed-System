# algorithms/ring.py
import sys
import time
import json

class RingAlgorithm:
    def __init__(self, nodes, node_id):
        self.nodes = sorted(nodes)
        self.node_id = node_id
        self.coordinator = None
        self.message_count = 0
        self.start_time = None

    def initiate_election(self):
        index = self.nodes.index(self.node_id)
        next_index = (index + 1) % len(self.nodes)
        next_node = self.nodes[next_index]
        
        self.message_count += 1
        print(f"Node {self.node_id} sends election message to {next_node}")
        self.handle_election_message(self.node_id, next_node)

    def handle_election_message(self, sender_id, receiver_id):
        index = self.nodes.index(receiver_id)
        next_index = (index + 1) % len(self.nodes)
        next_node = self.nodes[next_index]
        
        if receiver_id > sender_id:
            self.coordinator = receiver_id
        else:
            self.coordinator = sender_id
            
        self.message_count += 1
        print(f"Node {receiver_id} forwards election message to {next_node}")
        if next_node != self.node_id:
            self.handle_election_message(self.coordinator, next_node)
        else:
            self.announce_coordinator()

    def announce_coordinator(self):
        print(f"Node {self.coordinator} is elected as the coordinator")

    def run(self):
        self.start_time = time.time()
        self.initiate_election()
        end_time = time.time()
        self.store_metrics(end_time - self.start_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        metrics = {
            'node_id': self.node_id,
            'message_count': message_count,
            'convergence_time': convergence_time,
            'coordinator': self.coordinator
        }
        with open(f'metrics_ring_node_{self.node_id}.json', 'w') as file:
            json.dump(metrics, file, indent=4)
        print(f"Metrics saved for node {self.node_id}: {metrics}")

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    node_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    ring = RingAlgorithm(nodes, node_id)
    ring.run()
