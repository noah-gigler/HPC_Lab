#!/bin/bash
#SBATCH --job-name=hist      # Job name
#SBATCH --output=hist.out # Output file
#SBATCH --error=hist.err  # Error file
#SBATCH --ntasks=1               # Number of tasks
#SBATCH --constraint=EPYC_7763   # Select node with CPU
#SBATCH --cpus-per-task=4        # Number of CPUs per task
#SBATCH --mem-per-cpu=1024       # Memory per CPU
#SBATCH --time=01:00:00          # Wall clock time limit

# Load some modules & list loaded modules
module load gcc
module load python/3.11.6
module list

# Compile
make clean
make

# Run
python run_hist.py

