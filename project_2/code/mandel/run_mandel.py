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
        time_line = re.search(r'Total time:\s+([0-9.]+)', output)
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
    plt.savefig('mandel_strong.png')

def main():
    thread_counts = [2**i for i in range(8)]  # [1, 2, 4, 8, 16, 32, 64, 128]
    seq_time = run_program('./mandel_seq')
    par_times = [run_program('./mandel_par', num_threads) for num_threads in thread_counts]
    print('Sequential time:', seq_time)
    print('Parallel times:', par_times)
    speedups = [seq_time / par_time for par_time in par_times]

    plot_results(thread_counts, speedups)

def only_plot():
    thread_counts = [2**i for i in range(8)]
    with open("mandel.out", 'r') as file:
        content = file.read()

    seq_time_line = re.search(r'Sequential time:\s+([0-9.]+)', content)
    seq_time = float(seq_time_line.group(1)) if seq_time_line else None

    par_time_line = re.search(r'Parallel times:\s+\[([0-9.,\s]+)\]', content)
    par_times = [float(t) for t in par_time_line.group(1).split(',')] if par_time_line else []
    speedups = [seq_time / par_time for par_time in par_times]

    plot_results(thread_counts, speedups)

if __name__ == "__main__":
    only_plot()