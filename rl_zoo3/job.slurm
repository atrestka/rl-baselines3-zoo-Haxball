#!/bin/bash
#SBATCH --job-name=Trials_50_tasks_5_parallel_1v1
#SBATCH --nodes=1                
#SBATCH --ntasks=5           
#SBATCH --cpus-per-task=1        
#SBATCH --mem-per-cpu=1G         
#SBATCH --time=04:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-type=fail         # send email if job fails
#SBATCH --mail-user=atrestka@princeton.edu

module purge
module load anaconda3/2023.9

conda activate HaxballTrial

python train.py --algo dqn --env Haxball_1v1-v0 -n 100000 -optimize --study-name Trials_50_tasks_5_parallel_1v1