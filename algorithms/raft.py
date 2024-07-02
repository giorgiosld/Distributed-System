# algorithms/raft.py
import sys
import time
from kazoo.client import KazooClient

class RaftNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = 'Follower'
        self.current_term = 0
        self.voted_for = None
        self.message_count = 0
        self.start_time = time.time()
        self.zk = KazooClient(hosts='127.0.0.1:2181')
        self.zk.start()

    def become_candidate(self):
        self.state = 'Candidate'
        self.current_term += 1
        print(f"Node {self.node_id} becomes candidate for term {self.current_term}")
        self.voted_for = self.node_id
        self.request_votes()

    def request_votes(self):
        self.message_count += 1
        print(f"Node {self.node_id} is requesting votes")

    def receive_vote(self, term, candidate_id):
        self.message_count += 1
        if term > self.current_term:
            self.current_term = term
            self.voted_for = candidate_id
            print(f"Node {self.node_id} votes for {candidate_id} for term {term}")

    def run(self):
        self.start_time = time.time()
        self.become_candidate()
        end_time = time.time()
        print(f"Convergence Time: {end_time - self.start_time} seconds")
        print(f"Message Count: {self.message_count}")
        # Store metrics
        self.store_metrics(end_time - self.start_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        with open(f"metrics_raft.txt", "w") as f:
            f.write(f"Convergence Time: {convergence_time}\n")
            f.write(f"Message Count: {message_count}\n")

if __name__ == "__main__":
    node_id = int(sys.argv[1])
    node = RaftNode(node_id=node_id)
    node.run()
