#!/usr/bin/env bash
#SBATCH --job-name=scaling_anlysis
#SBATCH --output=scaling_analysis.stdout
#SBATCH --error=scaling-analysis.stderr
#SBATCH --ntasks=1
#SBATCH --constraint=EPYC_7763
#SBATCH --cpus-per-task=128
#SBATCH --mem-per-cpu=1024
#SBATCH --time=08:12:43

module load gcc
module load python/3.11.6

make -C sequential clean
make -C sequential

make -C parallel clean
make -C parallel

python scaling_analysis.py
