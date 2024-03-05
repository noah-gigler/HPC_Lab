import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

def plot_roofline_model(peak_flops_7763, peak_flops_7H12, peak_memory_bandwidth_7763, peak_memory_bandwidth_7H12):
    x = np.logspace(-5, 9, base=2)
    performance_7763 = np.minimum(x * peak_memory_bandwidth_7763, peak_flops_7763)
    performance_7H12 = np.minimum(x * peak_memory_bandwidth_7H12, peak_flops_7H12)

    fig, ax = plt.subplots()
    ax.plot(x, performance_7763, label='EPYC 7763')  
    ax.plot(x, performance_7H12, label='EPYC 7H12')
    ax.set_xscale('log', base=2)
    ax.set_yscale('log', base=2)
    ax.set_ylim(20, 50)
    plt.xlabel('Operational Intensity (FLOPS/byte)')
    plt.ylabel('Performance (GFLOPS)')
    plt.legend()
    plt.savefig('roofline_plot.png')

    print("Roofline plot saved as 'roofline_plot.png'")

if __name__ == "__main__":
    peak_flops_7763 = 39.2
    peak_flops_7H12 = 41.6
    peak_memory_bandwidth_7763 = 25
    peak_memory_bandwidth_7H12 = 20
    plot_roofline_model(peak_flops_7763, peak_flops_7H12, peak_memory_bandwidth_7763, peak_memory_bandwidth_7H12)

