#!/bin/bash
#SBATCH -J landcover_grassland
#SBATCH -A eecs
#SBATCH -o run.out
#SBATCH -e run.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=georgrog@oregonstate.edu
#SBATCH -t 6-12:30:00

##SBATCH --ntasks=8
#SBATCH --cpus-per-task=32
#SBATCH -p share,gpu,eecs

bash
export PATH=/nfs/guille/wong/wonglab4/rogen/conda/bin:$PATH
cd /nfs/guille/wong/wonglab4/rogen/conda/envs/conda_env_lab
source activate conda_env_lab

cd /nfs/hpc/share/georgrog/research/bird_presence
python driver.py
conda deactivate