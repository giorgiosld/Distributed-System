# algorithms/bully.py
import sys
import time
import json

class BullyAlgorithm:
    def __init__(self, nodes, node_id):
        self.nodes = nodes
        self.node_id = node_id
        self.coordinator = None
        self.message_count = 0
        self.start_time = None

    def initiate_election(self):
        highest_id = self.node_id
        for node in self.nodes:
            if node > self.node_id:
                self.message_count += 1
                print(f"Node {self.node_id} sends election message to {node}")
                response = self.handle_election_message(node)
                if response:
                    highest_id = max(highest_id, node)
        self.coordinator = highest_id
        if self.node_id == self.coordinator:
            print(f"Node {self.node_id} declares itself as the coordinator.")
        self.announce_coordinator()

    def handle_election_message(self, receiver):
        # Here, every node that receives an election message would start its own election
        if receiver > self.node_id:
            self.message_count += 1
            print(f"Node {receiver} responds to election from {self.node_id}")
            return True
        return False

    def announce_coordinator(self):
        for node in self.nodes:
            if node != self.coordinator:
                self.message_count += 1
                print(f"Node {self.coordinator} announces itself as coordinator to {node}")

    def run(self):
        self.start_time = time.time()
        self.initiate_election()
        end_time = time.time()
        convergence_time = end_time - self.start_time
        print(f"Convergence Time: {convergence_time} seconds")
        print(f"Message Count: {self.message_count}")
        self.store_metrics(convergence_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        metrics = {
            'node_id': self.node_id,
            'message_count': message_count,
            'convergence_time': convergence_time,
            'coordinator': self.coordinator
        }
        with open(f'metrics_bully_node_{self.node_id}.json', 'w') as file:
            json.dump(metrics, file, indent=4)
        print(f"Metrics saved for node {self.node_id}: {metrics}")

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    node_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1  # Default to node 1 if no input
    bully = BullyAlgorithm(nodes, node_id)
    bully.run()
