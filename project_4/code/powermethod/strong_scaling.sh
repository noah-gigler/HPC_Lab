#!/bin/bash
#SBATCH --job-name=power_strong      # Job name
#SBATCH --output=power_strong-%j.out # Output file
#SBATCH --error=power_strong-%j.err  # Error file
#SBATCH --ntasks=64                  # Number of tasks
#SBATCH --nodes=64                   # MULTI
#SBATCH --constraint=EPYC_7763       # Select node with CPU
#SBATCH --mem-per-cpu=1024           # Memory per CPU
#SBATCH --time=02:00:00              # Wall clock time limit
#SBATCH --mail-type=END

module load gcc
module load openmpi

make clean && make

TIME_FILE="strong_scaling_${SLURM_JOB_ID}.txt"
echo "n_threads, n_matrix, n_iters, theta, time" > $TIME_FILE

# Arguments
N=10000
n_iters=3000
test_case=3
tol=-0.000001 # -1e-6

for n_threads in 1 2 4 8 16 32 64
do 
    for rep in {1..5}
    do
        OUTPUT=$(mpirun -np $n_threads ./powermethod_rows $test_case $N $n_iters $tol)
        TIME=$(echo $OUTPUT | grep -o '### .* ###')
        LINE=$(echo $TIME | sed 's/### //g; s/ ###//g')
        echo "$LINE" >> $TIME_FILE
    done
    echo "Finished $n_threads threads"
done