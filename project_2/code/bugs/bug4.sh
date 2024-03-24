#!/bin/bash
#SBATCH --job-name=bug4  # Job name    (default: sbatch)
#SBATCH --output=bug4.out   # Output file (default: slurm-%j.out)
#SBATCH --error=bug4.err    # Error file  (default: slurm-%j.out)
#SBATCH --ntasks=1                # Number of tasks
#SBATCH --constraint=EPYC_7763    # Select node with CPU
#SBATCH --cpus-per-task=64       # Number of CPUs per task
#SBATCH --mem-per-cpu=1024        # Memory per CPU
#SBATCH --time=01:00:00           # Wall clock time limit

# Load some modules
module load gcc

module list

# Compile
make

ulimit -s 10000
OMP_NUM_THREADS=8
OMP_STACKSIZE=10M

./omp_bug4