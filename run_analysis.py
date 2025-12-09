import time
import os
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


def test_tree(tree_cls, data):
    """构建树并返回 (耗时ms, 高度)"""
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
        avl_t, avl_h = test_tree(AVLTree, data)
        results['avl_time'].append(avl_t)
        results['avl_height'].append(avl_h)


        if "random" in file_prefix or n <= MAX_BST_SAFE_SIZE:
            bst_t, bst_h = test_tree(BSTTree, data)
        else:
            print(f"  Skipping BST for N={n} (Too large for Worst Case)")
            bst_t, bst_h = None, None  # 标记为 None

        results['bst_time'].append(bst_t)
        results['bst_height'].append(bst_h)
        b_t_str = f"{bst_t:.2f}" if bst_t is not None else "N/A"
        b_h_str = str(bst_h) if bst_h is not None else "N/A"
        print(f"Size {n:<6} | AVL: {avl_t:.2f}ms (H={avl_h}) | BST: {b_t_str}ms (H={b_h_str})")

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
    ax1.plot(sizes, results['bst_time'], marker='o', color='red', linestyle='--',
             label='BST')

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
    print(f"Saved chart: {filename}")
    plt.close()


def main():
    if not os.path.exists(DATA_DIR):
        print("Data directory not found. Please run generate_data.py first!")
        return

    res_rand = run_scenario("Random", "random")
    plot_scenario(res_rand, "Random", "analysis_random.png")
    res_sort = run_scenario("Sorted", "sorted")
    plot_scenario(res_sort, "Sorted (Worst Case)", "analysis_sorted.png")
    res_rev = run_scenario("Reverse Sorted", "reverse")
    plot_scenario(res_rev, "Reverse Sorted", "analysis_reverse.png")


if __name__ == "__main__":
    main()