# visualizer.py
import json
import matplotlib.pyplot as plt
import os
import glob

def read_metrics(algorithm):
    # This assumes your JSON files are named like 'metrics_<algorithm>_node_<node_id>.json'
    files = glob.glob(f'metrics_{algorithm}_node_*.json')
    data = {'convergence_time': [], 'message_count': [], 'node_id': []}
    for file in files:
        with open(file, 'r') as f:
            metrics = json.load(f)
            data['convergence_time'].append(metrics['convergence_time'])
            data['message_count'].append(metrics['message_count'])
            data['node_id'].append(metrics['node_id'])
    return data

def plot_data(data, algorithm):
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Node ID')
    ax1.set_ylabel('Convergence Time (s)', color=color)
    ax1.bar(data['node_id'], data['convergence_time'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel('Message Count', color=color)  # we already handled the x-label with ax1
    ax2.plot(data['node_id'], data['message_count'], color=color, marker='o', linestyle='dashed')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title(f'Performance Metrics for {algorithm} Algorithm')
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    # Save the plot as an image file
    plot_filename = f'plot_{algorithm}.png'
    plt.savefig(plot_filename)
    print(f"Plot saved as {plot_filename}")

def main():
    algorithms = ['bully', 'ring', 'proof_of_work', 'proof_of_stake']
    for alg in algorithms:
        data = read_metrics(alg)
        if data['node_id']:  # Only plot if there is data
            plot_data(data, alg)

if __name__ == '__main__':
    main()
