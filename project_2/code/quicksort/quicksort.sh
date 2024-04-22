#!/bin/bash

#SBATCH --job-name=quicksort
#SBATCH --output=quicksort.out   # Output file
#SBATCH --error=quicksort.err    # Error file
#SBATCH --ntasks=1                # Number of tasks
#SBATCH --constraint=EPYC_7763    # Select node with CPU
#SBATCH --cpus-per-task=128       # Number of CPUs per task
#SBATCH --mem-per-cpu=1024        # Memory per CPU
#SBATCH --time=01:00:00           # Wall clock time limit

module load gcc

make clean
make

echo "Sequential"
./quicksort_seq

echo "Parallel"
export OMP_NUM_THREADS=32
./quicksort_par