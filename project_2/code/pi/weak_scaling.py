import re

import matplotlib.pyplot as plt
import numpy as np

type = "weak"

with open('pi_'+ type + '.out', 'r') as file:
    data = file.read()

regex = r"time = (\d+\.\d+) secs"

# Find all matches
matches = re.findall(regex, data)

# Split matches into critical, reduction, and serial times
critical_times = matches[:-9:2]  # even indices, excluding the last two
reduction_times = matches[1:-8:2]  # odd indices, excluding the last one
serial_time = matches[-8:]  # last index

threads = [1, 2, 4, 8, 16, 32, 64, 128]

critical_times = np.array(critical_times, dtype=float)
reduction_times = np.array(reduction_times, dtype=float)
serial_times = np.array(serial_time, dtype=float)


# Calculate speedup
speedup_critical = critical_times/serial_times
speedup_reduction = reduction_times/serial_times

# Plotting
plt.plot(threads, speedup_critical, label='Speedup (Critical)')
plt.plot(threads, speedup_reduction, label='Speedup (Reduction)')
plt.xlabel('Thread Count')
plt.ylabel('Speedup')
plt.title('Speedup vs Thread Count')

plt.legend()
plt.savefig(f'{type}_scaling.png', dpi=500)
