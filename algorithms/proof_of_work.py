# algorithms/proof_of_work.py
import hashlib
import time

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.message_count = 0
        self.start_time = time.time()

    def mine(self, block):
        block_nonce = 0
        while not self.is_valid_nonce(block, block_nonce):
            self.message_count += 1
            block_nonce += 1
        return block_nonce

    def is_valid_nonce(self, block, nonce):
        hash_result = hashlib.sha256(f"{block}{nonce}".encode()).hexdigest()
        return hash_result[:self.difficulty] == '0' * self.difficulty

    def run(self):
        block = "Sample Block"
        self.start_time = time.time()
        nonce = self.mine(block)
        end_time = time.time()
        print(f"Block mined with nonce: {nonce}")
        print(f"Convergence Time: {end_time - self.start_time} seconds")
        print(f"Message Count: {self.message_count}")
        # Store metrics
        self.store_metrics(end_time - self.start_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        with open(f"metrics_proof_of_work.txt", "w") as f:
            f.write(f"Convergence Time: {convergence_time}\n")
            f.write(f"Message Count: {message_count}\n")

if __name__ == "__main__":
    pow = ProofOfWork(difficulty=4)
    pow.run()
