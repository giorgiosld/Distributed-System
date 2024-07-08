import json
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd

def read_metrics(algorithm):
    files = glob.glob(f'metrics_{algorithm}_node_*.json')
    data = {'convergence_time': [], 'message_count': [], 'node_id': []}
    for file in files:
        with open(file, 'r') as f:
            metrics = json.load(f)
            data['convergence_time'].append(metrics['convergence_time'])
            data['message_count'].append(metrics['message_count'])
            data['node_id'].append(metrics['node_id'])
    return data

def plot_average_convergence_time(data):
    algorithms = list(data.keys())
    averages = [np.mean(data[alg]['convergence_time']) for alg in algorithms]
    
    fig, ax = plt.subplots()
    ax.bar(algorithms, averages, color='lightblue')
    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Average Convergence Time (s)')
    ax.set_title('Average Convergence Time by Algorithm')

    # Add a table below the chart
    cell_text = [[f"{np.mean(data[alg]['convergence_time']):.4f}"] for alg in algorithms]
    table = plt.table(cellText=cell_text, rowLabels=algorithms, colLabels=['Average Time (s)'],
                      cellLoc='center', rowLoc='center', loc='bottom', bbox=[0.25, -0.6, 0.5, 0.5])
    plt.subplots_adjust(left=0.2, bottom=0.4)
    plt.show()

def create_pandas_table(data):
    df_list = []
    for alg, metrics in data.items():
        if alg in ['bully', 'ring']:
            notation = r'$O(n^2)$' if alg == 'bully' else r'$O(n)$'
            df = pd.DataFrame({
                'Algorithm': [alg] * len(metrics['convergence_time']),
                'Node ID': metrics['node_id'],
                'Convergence Time': metrics['convergence_time'],
                'Message Count': metrics['message_count'],
                'O Notation': [notation] * len(metrics['convergence_time'])
            })
        else:
            df = pd.DataFrame({
                'Algorithm': [alg] * len(metrics['convergence_time']),
                'Node ID': metrics['node_id'],
                'Convergence Time': metrics['convergence_time']
            })
        df_list.append(df)
    df_all = pd.concat(df_list, ignore_index=True)
    return df_all

def save_table_as_image(df, filename):
    fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as needed
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    plt.savefig(filename, bbox_inches='tight')

def plot_distribution(data):
    fig, ax = plt.subplots()
    for alg, metrics in data.items():
        convergence_times = metrics['convergence_time']
        ax.hist(convergence_times, bins=10, alpha=0.5, label=alg)
    ax.set_xlabel('Convergence Time (s)')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Convergence Times')
    ax.legend(loc='best')
    plt.show()

def main():
    algorithms = ['bully', 'ring', 'pow', 'pos']
    all_data = {}

    for alg in algorithms:
        data = read_metrics(alg)
        if data['node_id']:
            all_data[alg] = data

    if all_data:
        plot_average_convergence_time(all_data)
        df_all = create_pandas_table(all_data)
        save_table_as_image(df_all, 'convergence_times_table.png')
        plot_distribution(all_data)

if __name__ == '__main__':
    main()
