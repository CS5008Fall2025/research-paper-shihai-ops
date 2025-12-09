import random
import os

OUTPUT_DIR = "test_data"
SIZES = [100, 500, 1000, 2000, 5000, 10000]

def ensure_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def save_file(filename, data):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write('\n'.join(map(str, data)))
    print(f"Generated: {filename} (N={len(data)})")

def main():
    ensure_dir()

    for n in SIZES:
        data_random = list(range(n))
        random.shuffle(data_random)
        save_file(f"random_{n}.txt", data_random)

        data_sorted = list(range(n))
        save_file(f"sorted_{n}.txt", data_sorted)

        data_reverse = list(range(n-1, -1, -1))
        save_file(f"reverse_{n}.txt", data_reverse)

    print("\nAll data generation complete!")

if __name__ == "__main__":
    main()