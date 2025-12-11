import time
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from trees import BSTTree, AVLTree

DATA_DIR = "test_data"
SIZES = [100, 500, 1000, 2000, 5000, 10000]
MAX_BST_SAFE_SIZE = 2500

plt.style.use('ggplot')


def load_data(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return []
    with open(path, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]


def save_results_to_csv(results, scenario_name):
    safe_name = scenario_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    time_filename = f"analysis_{safe_name}_runtime.csv"
    with open(time_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Input Size (N)', 'BST Time (ms)', 'AVL Time (ms)'])
        for i in range(len(results['sizes'])):
            n = results['sizes'][i]
            bst_t = results['bst_time'][i] if results['bst_time'][i] is not None else ""
            avl_t = results['avl_time'][i]
            writer.writerow([n, bst_t, avl_t])

    print(f"  [CSV] Saved runtime data to: {time_filename}")
    height_filename = f"analysis_{safe_name}_height.csv"
    with open(height_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Input Size (N)', 'BST Height', 'AVL Height'])

        for i in range(len(results['sizes'])):
            n = results['sizes'][i]
            bst_h = results['bst_height'][i] if results['bst_height'][i] is not None else ""
            avl_h = results['avl_height'][i]
            writer.writerow([n, bst_h, avl_h])

    print(f"  [CSV] Saved height data to:  {height_filename}")


def test_tree(tree_cls, data):
    tree = tree_cls()
    start = time.time()
    try:
        for x in data:
            tree.insert(x)
    except RecursionError:
        return None, None

    end = time.time()

    if hasattr(tree, 'get_tree_height'):
        h = tree.get_tree_height()
    else:
        h = tree.get_height()

    return (end - start) * 1000, h


def run_scenario(scenario_name, file_prefix):
    print(f"\n--- Running Analysis for: {scenario_name} ---")

    results = {
        'sizes': SIZES,
        'bst_time': [], 'avl_time': [],
        'bst_height': [], 'avl_height': []
    }

    for n in SIZES:
        filename = f"{file_prefix}_{n}.txt"
        data = load_data(filename)

        # Test AVL
        avl_t, avl_h = test_tree(AVLTree, data)
        results['avl_time'].append(avl_t)
        results['avl_height'].append(avl_h)

        # Test BST
        if "random" in file_prefix or n <= MAX_BST_SAFE_SIZE:
            bst_t, bst_h = test_tree(BSTTree, data)
        else:
            print(f"  Skipping BST for N={n} (Too large)")
            bst_t, bst_h = None, None

        results['bst_time'].append(bst_t)
        results['bst_height'].append(bst_h)
        b_t_str = f"{bst_t:.2f}" if bst_t is not None else "N/A"
        print(f"Size {n:<6} | AVL: {avl_t:.2f}ms | BST: {b_t_str}ms")

    return results


def plot_scenario(results, scenario_name, filename):
    sizes = results['sizes']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle(f'Analysis: {scenario_name} Data Input', fontsize=16)
    ax1.plot(sizes, results['bst_time'], marker='o', color='red', linestyle='--', label='BST')
    ax1.plot(sizes, results['avl_time'], marker='s', color='green', linewidth=2, label='AVL')
    ax1.set_xlabel('Input Size (N)')
    ax1.set_ylabel('Construction Time (ms)')
    ax1.set_title('Time Complexity')
    ax1.legend()
    ax1.grid(True)
    ax1.plot(sizes, results['bst_time'], marker='o', color='red', linestyle='--', label='BST')
    ax2.plot(sizes, results['bst_height'], marker='o', color='red', linestyle='--', label='BST Height')
    ax2.plot(sizes, results['avl_height'], marker='s', color='green', linewidth=2, label='AVL Height')
    ideal_h = [np.log2(n) for n in sizes]
    ax2.plot(sizes, ideal_h, color='gray', linestyle=':', alpha=0.5, label='Log2(N) Reference')
    ax2.set_xlabel('Input Size (N)')
    ax2.set_ylabel('Tree Height')
    ax2.set_title('Height Analysis (Balance)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"  [Chart] Saved chart: {filename}")
    plt.close()


def main():
    if not os.path.exists(DATA_DIR):
        print("Data directory not found. Please run generate_data.py first!")
        return

    scenarios = [
        ("Random", "random", "analysis_random.png"),
        ("Sorted", "sorted", "analysis_sorted.png"),
        ("Reverse Sorted", "reverse", "analysis_reverse.png")
    ]

    for name, prefix, img_file in scenarios:
        results = run_scenario(name, prefix)
        plot_scenario(results, name, img_file)
        save_results_to_csv(results, name)


if __name__ == "__main__":
    main()