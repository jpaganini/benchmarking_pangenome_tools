#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=ggcaller
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

# Run ggcaller
ggcaller --refs ../../2023_10_raw_data/results/ggcaller_result/ggcaller_input.txt --out ../../2023_10_raw_data/results/ggcaller_result --threads 16
