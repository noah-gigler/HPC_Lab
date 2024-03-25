import subprocess
import re
import numpy as np
import matplotlib.pyplot as plt
import os

def run_program(program_name, num_threads=None):
    times = []
    for _ in range(10):
        env = os.environ.copy()
        if num_threads:
            env['OMP_NUM_THREADS'] = str(num_threads)
        result = subprocess.run(program_name, env=env, capture_output=True, text=True, shell=True)
        output = result.stdout
        time_line = re.search(r'Time: ([0-9.]+) sec', output)
        if time_line:
            time = float(time_line.group(1))
            times.append(time)
    return np.mean(times)

def plot_results(thread_counts, speedups):
    plt.figure(figsize=(10, 5))
    plt.plot(thread_counts, speedups, marker='o')
    plt.title('Speedup: Parallel vs Sequential')
    plt.xlabel('Number of Threads')
    plt.ylabel('Speedup')
    plt.grid(True)
    plt.savefig('histogram_strong.png')

def main():
    thread_counts = [2**i for i in range(8)]  # [1, 2, 4, 8, 16, 32, 64, 128]
    seq_time = run_program('./hist_omp')
    par_times = [run_program('./hist_omp', num_threads) for num_threads in thread_counts]
    print('Sequential time:', seq_time)
    print('Parallel times:', par_times)
    speedups = [seq_time / par_time for par_time in par_times]

    plot_results(thread_counts, speedups)

if __name__ == "__main__":
    main()