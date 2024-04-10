#!/bin/bash
#SBATCH --job-name=pleaseWorkv0
#SBATCH --nodes=1                
#SBATCH --ntasks=1               
#SBATCH --cpus-per-task=1        
#SBATCH --mem-per-cpu=4G         
#SBATCH --time=02:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-type=fail         # send email if job fails
#SBATCH --mail-user=atrestka@princeton.edu

module purge
module load anaconda3/2023.9

conda activate HaxballTrial



python train.py --algo dqn --env SinglePlayerHaxball-v0 -optimize --n-trials 3 --study-name HBHPv1.1 --storage "sqlite:///HBHPv1.1"