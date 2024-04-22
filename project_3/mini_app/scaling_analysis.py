import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
import re

def plot_strong_speedup(thread_counts: np.array, serial_time: float, parallel_times: np.array, identifier: str):
  parallel_speedup = serial_time / np.array(parallel_times)
  
  plt.clf()
  plt.plot(thread_counts, parallel_speedup)
  plt.xlabel('nthreads')
  plt.ylabel('speedup')
  plt.legend()
  plt.title('Strong Scaling Speedup')
  plt.savefig(f'strong_scaling_{identifier}.pdf')

def plot_weak_speedup(thread_counts: np.array, serial_times: np.array, parallel_times: np.array, identifier: str):
  parallel_speedup = np.array(serial_times) / np.array(parallel_times)
  
  plt.clf()
  plt.plot(thread_counts, parallel_speedup)
  plt.xlabel('nthreads')
  plt.ylabel('speedup')
  plt.legend()
  plt.title('Weak Scaling Speedup')
  plt.savefig(f'weak_scaling_{identifier}.pdf')

def runtime(exec_path: str, nthreads: int, load: int) -> float:
  env = {'OMP_NUM_THREADS': str(nthreads)}
  result = sp.run([exec_path, str(load), "100", "0.005"], env=env, stdout=sp.PIPE)
  output = result.stdout.decode('utf-8')
  
  time = re.search(r'simulation took ([0-9.]+) seconds', output)
  time = float(time.group(1))
  return time

def average_runtime_constant_load(exec_path: str, nthreads: int, nruns: int, load: int) -> float:
  return sum([runtime(exec_path, nthreads, load) for _ in range(nruns)]) / nruns

def average_runtime_proportional_load(exec_path: str, nthreads: int, nruns: int, base_load: int) -> float:
  return sum([runtime(exec_path, nthreads, base_load * nthreads) for _ in range(nruns)]) / nruns

if __name__ == "__main__":
  nruns = 5

  # loads = [64, 128, 256, 512, 1024]
  # for load in loads:
  #   serial_time = average_runtime_constant_load("./sequential/main", 1, nruns, load)

  #   thread_counts = [1, 2, 4, 8, 16]
  #   parallel_times = []
  #   for nthreads in thread_counts:
  #     parallel_times.append(average_runtime_constant_load("./parallel/main", nthreads, nruns, load))
   
  #   plot_strong_speedup(thread_counts, serial_time, parallel_times, str(load)) 

  loads = [64, 128, 256]
  for load in loads:

    thread_counts = [1,4,16,64]
    serial_times = []
    parallel_times = []
    for nthreads in thread_counts:
      serial_times.append(average_runtime_proportional_load("./sequential/main", nthreads, nruns, load))
      parallel_times.append(average_runtime_proportional_load("./parallel/main", nthreads, nruns, load))
   
    plot_weak_speedup(thread_counts, serial_times, parallel_times, str(load)) 
    

