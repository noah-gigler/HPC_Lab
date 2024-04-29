#!/bin/bash
#SBATCH --job-name=power_weak      # Job name
#SBATCH --output=power_weak-%j.out # Output file
#SBATCH --error=power_weak-%j.err  # Error file
#SBATCH --ntasks=64                  # Number of tasks
#SBATCH --nodes=1                   # MULTI
#SBATCH --constraint=EPYC_7763       # Select node with CPU
#SBATCH --mem-per-cpu=1024           # Memory per CPU
#SBATCH --time=05:00:00              # Wall clock time limit
#SBATCH --mail-type=END

module load gcc
module load openmpi

make clean && make

TIME_FILE="weak_scaling_single1.txt"
echo "n_threads, n_matrix, n_iters, theta, time" > $TIME_FILE

# Arguments
n_iters=3000
test_case=3
tol=-0.000001 # -1e-6

threads=(1 2 4 8 16 32 64)
N_vals=(1000 1414 2000 2828 4000 5657 8000)

for i in {0..6}
do 
    N=${N_vals[$i]}
    n_threads=${threads[$i]}

    for rep in {1..10}
    do
        OUTPUT=$(mpirun -np $n_threads ./powermethod_rows $test_case $N $n_iters $tol)
        TIME=$(echo $OUTPUT | grep -o '### .* ###')
        LINE=$(echo $TIME | sed 's/### //g; s/ ###//g')
        echo "$LINE" >> $TIME_FILE
    done
    echo "Finished $n_threads threads"
done