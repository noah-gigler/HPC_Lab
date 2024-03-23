#!/bin/bash
#SBATCH --job-name=pi      # Job name    (default: sbatch)
#SBATCH --output=pi_weak.out # Output file (default: slurm-%j.out)
#SBATCH --error=pi_weak.err  # Error file  (default: slurm-%j.out)
#SBATCH --ntasks=1                # Number of tasks
#SBATCH --constraint=EPYC_7763    # Select node with CPU
#SBATCH --cpus-per-task=48       # Number of CPUs per task
#SBATCH --mem-per-cpu=1024        # Memory per CPU
#SBATCH --time=00:05:00           # Wall clock time limit

# Load some modules & list loaded modules
module load gcc
module list

# Compile
make clean
make

# Run the program for OMP_NUM_THREADS equal to 1, 2, 4, 8, ..., 64, 128
for ((i=0; i<=7; i++))
do
    OMP_NUM_THREADS=$((2**i))
    PROBLEM_SIZE=$((OMP_NUM_THREADS*1000000))
    echo "Running with OMP_NUM_THREADS=$OMP_NUM_THREADS"
    export OMP_NUM_THREADS
    ./pi_omp_critical PROBLEM_SIZE
    ./pi_omp_reduction PROBLEM_SIZE
done

for ((i=0; i<=7; i++))
do
    OMP_NUM_THREADS=$((2**i))
    PROBLEM_SIZE=$((OMP_NUM_THREADS*1000000))
    echo "serial"
    ./pi_serial 
done