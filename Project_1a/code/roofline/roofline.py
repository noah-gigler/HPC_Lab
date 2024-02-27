import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

def plot_roofline_model(peak_flops_7763, peak_flops_7H12, peak_memory_bandwidth_7763, peak_memory_bandwidth_7H12):
    x = np.logspace(np.log2(1/4), np.log2(128), base=2)
    performance_7763 = np.minimum(x * peak_memory_bandwidth_7763, peak_flops_7763)
    performance_7H12 = np.minimum(x * peak_memory_bandwidth_7H12, peak_flops_7H12)

    plt.loglog(x, performance_7763, label='EPYC 7763')  
    plt.loglog(x, performance_7H12, label='EPYC 7H12')
    plt.xlabel('Operational Intensity (FLOPS/byte)')
    plt.ylabel('Performance (GFLOPS)')
    plt.legend()
    plt.savefig('roofline_plot.png')

    print("Roofline plot saved as 'roofline_plot.png'")

if __name__ == "__main__":
    plot_roofline_model(41.6, 39.2, 25, 22)

