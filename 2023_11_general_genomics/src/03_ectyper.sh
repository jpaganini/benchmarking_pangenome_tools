#!/bin/bash

#sbatch details
#SBATCH --time=48:00:00
#SBATCH --mem=16G
#SBATCH -c 8
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=ecoli_serotyping
#SBATCH --error=slurm-%j_ectyper.err
#SBATCH --output=slurm-%j_ectyper.out

#Pass the miniconda3 installation directory and activate the right environment.

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate ectyper        

#----------------------------------------- run the predictions------------------------------------------#

mkdir ../results/ectyper

#run ectyper (-c argument could be removed, -o location should be change as well)

ectyper -i ../data/complete_genomes/ecoli -c 8 -o ../results/ectyper


