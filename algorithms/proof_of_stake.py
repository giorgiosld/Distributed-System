# algorithms/proof_of_stake.py
import random
import time

class ProofOfStake:
    def __init__(self, stakeholders):
        self.stakeholders = stakeholders
        self.message_count = 0
        self.start_time = time.time()

    def select_validator(self):
        total_stake = sum(self.stakeholders.values())
        random_choice = random.uniform(0, total_stake)
        cumulative = 0
        for stakeholder, stake in self.stakeholders.items():
            self.message_count += 1
            cumulative += stake
            if cumulative >= random_choice:
                return stakeholder

    def run(self):
        self.start_time = time.time()
        validator = self.select_validator()
        end_time = time.time()
        print(f"Selected validator: {validator}")
        print(f"Convergence Time: {end_time - self.start_time} seconds")
        print(f"Message Count: {self.message_count}")
        # Store metrics
        self.store_metrics(end_time - self.start_time, self.message_count)

    def store_metrics(self, convergence_time, message_count):
        with open(f"metrics_proof_of_stake.txt", "w") as f:
            f.write(f"Convergence Time: {convergence_time}\n")
            f.write(f"Message Count: {message_count}\n")

if __name__ == "__main__":
    stakeholders = {'Node1': 50, 'Node2': 30, 'Node3': 20}
    pos = ProofOfStake(stakeholders)
    pos.run()
