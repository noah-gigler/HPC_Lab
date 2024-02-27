#!/bin/bash
#SBATCH --job-name=slurm_stream     # Job name    (default: sbatch)
#SBATCH --output=slurm_stream.out # Output file (default: slurm-%j.out)
#SBATCH --error=slurm_stream.err # Error file  (default: slurm-%j.out)
#SBATCH --ntasks=1                    # Number of tasks
#SBATCH --cpus-per-task=1             # Number of CPUs per task
#SBATCH --mem-per-cpu=2048            # Memory per CPU
#SBATCH --time=00:01:00               # Wall clock time limit
#SBATCH --constraint=EPYC_7H12


module load gcc # load a compiler (gcc/11.4.0)

#32MB/8bytes * 4 = 16M
gcc -O3 -march=native -DSTREAM_TYPE=double -DSTREAM_ARRAY_SIZE=20000000 \
-DNTIMES=20 stream.c -o stream_c.exe # compile

# get job id
job_id=$(sbatch --mem-per-cpu=2G --wrap "./stream_c.exe > slurm_output.txt" | awk '{print $4}')

# wait until finished
while squeue -j $job_id | grep -q $job_id
do
    sleep 1
done

# get relevant results
grep -E "Copy:|Scale:|Add:|Triad:|Function" slurm_output.txt > output.txt

# clean up
rm slurm_stream.err slurm_stream.out temp.txt stream_c.exe slurm-"$job_id".out

