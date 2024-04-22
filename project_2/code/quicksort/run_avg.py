import numpy as np
import matplotlib.pyplot as plt
import re
import subprocess as sp

def plot_strong_scaling(serial_avg, parallel_avg, nthreads):
    parallel_speedup = np.array(serial_avg)  / np.array(parallel_avg)

    plt.plot(nthreads, parallel_speedup)
    plt.xlabel('nthreads')
    plt.ylabel('speedup')
    plt.title('Strong scaling')
    plt.savefig('plot-strong.png')

def run_strong(n_threads, exe_path, n_runs, time_average):
    total_time = 0
    total_iter = 0
    total_flop = 0
    env = {'OMP_NUM_THREADS': str(n_threads)}

    for _ in range(n_runs):
        result = sp.run([exe_path], env=env, stdout=sp.PIPE)
        output = result.stdout.decode('utf-8')
        print(output) 

        match_time = re.search(r'elapsed time\[s\]\s+([\d.]+[eE][+\-]?\d+)', output)
        if match_time:
            time_str = match_time.group(1)
            time = float(time_str)
            total_time += time
            
    time_average.append(total_time / n_runs)
      
if __name__ == "__main__":
    serial_time_average_strong = []
    parallel_time_average_strong = []

    n_threads = []

    print("Strong Scaling")
    for i in range(8):
        num_threads = 2 ** i
        n_threads.append(num_threads)
        
        print(f"Running with OMP_NUM_THREADS = {num_threads}")         
        print("Serial")
        run_strong(num_threads, "./quicksort_seq", 10, serial_time_average_strong)
        
        print("Parallel")
        run_strong(num_threads, "./quicksort_par", 10, parallel_time_average_strong)
        
    plot_strong_scaling(serial_time_average_strong, 
        parallel_time_average_strong, 
        n_threads)

