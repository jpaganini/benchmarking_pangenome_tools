#!/bin/bash

#sbatch details
#SBATCH --time=3:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=bifrost
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

# Run bifrost
Bifrost build -t 16 -k 31 -s ../../../../2023_10_raw_data/results/bifrost_result/bifrost_input.txt  -o ../../../../2023_10_raw_data/results/bifrost_result/bifrost_graph
