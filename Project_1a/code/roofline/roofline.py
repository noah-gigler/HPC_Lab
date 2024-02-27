import matplotlib.pyplot as plt
import numpy as np

def plot_roofline_model(peak_flops, peak_memory_bandwidth):
    # Create x-axis data points
    x = np.linspace(0, peak_flops, 100)

    # Calculate roofline boundaries
    roofline_flops = np.minimum(x, peak_flops)
    roofline_memory_bandwidth = np.minimum(x * peak_memory_bandwidth, peak_memory_bandwidth)

    # Plot the roofline model
    plt.plot(x, roofline_flops, label='Roofline FLOPS')
    plt.plot(x, roofline_memory_bandwidth, label='Roofline Memory Bandwidth')

    # Set plot labels and legend
    plt.xlabel('FLOPS')
    plt.ylabel('Memory Bandwidth')
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Define the input parameters
    peak_flops = 41.6
    peak_memory_bandwidth = 25

    # Call the plot_roofline_model function
    plot_roofline_model(peak_flops, peak_memory_bandwidth)

