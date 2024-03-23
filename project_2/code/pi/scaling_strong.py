import re

import matplotlib.pyplot as plt

type = "strong"

with open('pi_'+ type + '.out', 'r') as file:
    data = file.read()

regex = r"time = (\d+\.\d+) secs"

# Find all matches
matches = re.findall(regex, data)

# Split matches into critical, reduction, and serial times
critical_times = matches[:-2:2]  # even indices, excluding the last two
reduction_times = matches[1:-1:2]  # odd indices, excluding the last one
serial_time = matches[-1]  # last index

threads = [1, 2, 4, 8, 16, 32, 64, 128]

# Calculate speedup
speedup_critical = [float(serial_time) / float(time) for time in critical_times]
speedup_reduction = [float(serial_time) / float(time) for time in reduction_times]

# Plotting
plt.plot(threads, speedup_critical, label='Speedup (Critical)')
plt.plot(threads, speedup_reduction, label='Speedup (Reduction)')
plt.xlabel('Thread Count')
plt.ylabel('Speedup')
plt.title('Speedup vs Thread Count')

plt.legend()
plt.savefig(f'{type}_scaling.png', dpi=500)
