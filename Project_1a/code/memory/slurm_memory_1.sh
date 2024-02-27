#!/bin/bash
#SBATCH --job-name=slurm_memory     # Job name    (default: sbatch)
#SBATCH --output=slurm_memory1.out # Output file (default: slurm-%j.out)
#SBATCH --error=slurm_memory1.err  # Error file  (default: slurm-%j.out)
#SBATCH --nodes=1                     # Number of nodes
#SBATCH --ntasks=1                    # Number of tasks
#SBATCH --cpus-per-task=1             # Number of CPUs per task
#SBATCH --mem-per-cpu=1024            # Memory per CPU
#SBATCH --time=00:01:00               # Wall clock time limit
#SBATCH --constraint=EPYC_7H12

lscpu | grep "Model name"

cat /proc/meminfo | grep "MemTotal"

hwloc-ls --whole-system --no-io