# algorithms/bully.py
import sys
import time
from kazoo.client import KazooClient

class BullyAlgorithm:
    def __init__(self, nodes, node_id):
        self.nodes = nodes
        self.node_id = node_id
        self.coordinator = None
        self.message_count = 0
        self.start_time = time.time()

    def start_election(self):
        for node in self.nodes:
            if node > self.node_id:
                self.message_count += 1
                print(f"Node {self.node_id} sends election message to {node}")
                self.send_message(node, "ELECTION")
        self.coordinator = self.node_id

    def send_message(self, node, message):
        if message == "ELECTION":
            if node > self.node_id:
                self.message_count += 1
                print(f"Node {node} responds to election from {self.node_id}")
                self.coordinator = node
                self.start_election()

    def announce_coordinator(self):
        for node in self.nodes:
            if node != self.coordinator:
                self.message_count += 1
                print(f"Node {self.coordinator} announces itself as coordinator to {node}")

    def run(self):
        self.start_time = time.time()
        self.start_election()
        self.announce_coordinator()
        end_time = time.time()
        print(f"Convergence Time: {end_time - self.start_time} seconds")
        print(f"Message Count: {self.message_count}")
        # Store metrics
        self.store_metrics(end_time - self.start_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        with open(f"metrics_bully.txt", "w") as f:
            f.write(f"Convergence Time: {convergence_time}\n")
            f.write(f"Message Count: {message_count}\n")

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    node_id = int(sys.argv[1])
    bully = BullyAlgorithm(nodes, node_id)
    bully.run()
