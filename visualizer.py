# visualizer.py

import os
import numpy as np
import matplotlib.pyplot as plt

def read_metrics(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()
        convergence_time = float(data[0].split(": ")[1].strip())
        message_count = int(data[1].split(": ")[1].strip())
    return convergence_time, message_count

def gather_metrics():
    algorithms = ["bully", "raft", "proof_of_work", "proof_of_stake"]
    metrics = {}

    for algorithm in algorithms:
        file_path = f"metrics_{algorithm}.txt"

        if os.path.exists(file_path):
            convergence_time, message_count = read_metrics(file_path)
            metrics[algorithm] = {
                "Convergence Time": convergence_time,
                "Message Count": message_count
            }
        else:
            print(f"Metrics file for {algorithm} not found.")

    return metrics

def plot_metrics(metrics):
    algorithms = list(metrics.keys())
    convergence_times = [metrics[alg]["Convergence Time"] for alg in algorithms]
    message_counts = [metrics[alg]["Message Count"] for alg in algorithms]

    x = np.arange(len(algorithms))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Algorithms')
    ax1.set_ylabel('Convergence Time (s)', color=color)
    ax1.bar(x - width/2, convergence_times, width, label='Convergence Time', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:red'
    ax2.set_ylabel('Message Count', color=color)
    ax2.bar(x + width/2, message_counts, width, label='Message Count', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax1.set_xticks(x)
    ax1.set_xticklabels(algorithms)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.title('Leader Election Algorithms Comparison')
    plt.show()

if __name__ == "__main__":
    metrics = gather_metrics()
    if metrics:
        plot_metrics(metrics)
