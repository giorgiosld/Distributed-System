# algorithms/proof_of_work.py
import sys
import time
import random
import hashlib
import json

class ProofOfWorkAlgorithm:
    def __init__(self, node_id):
        self.node_id = node_id
        self.message_count = 0
        self.start_time = None

    def mine_block(self, difficulty=4):
        prefix = '0' * difficulty
        nonce = 0
        while True:
            nonce += 1
            self.message_count += 1
            block_content = f"{self.node_id}-{nonce}".encode()
            block_hash = hashlib.sha256(block_content).hexdigest()
            if block_hash.startswith(prefix):
                print(f"Node {self.node_id} mined a block with nonce {nonce}")
                return nonce

    def run(self):
        self.start_time = time.time()
        nonce = self.mine_block()
        end_time = time.time()
        self.store_metrics(end_time - self.start_time, self.message_count, nonce)

    def store_metrics(self, convergence_time, message_count, nonce):
        metrics = {
            'node_id': self.node_id,
            'message_count': message_count,
            'convergence_time': convergence_time,
            'nonce': nonce
        }
        with open(f'metrics_pow_node_{self.node_id}.json', 'w') as file:
            json.dump(metrics, file, indent=4)
        print(f"Metrics saved for node {self.node_id}: {metrics}")

if __name__ == "__main__":
    node_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    pow = ProofOfWorkAlgorithm(node_id)
    pow.run()
