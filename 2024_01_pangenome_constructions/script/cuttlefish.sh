#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=30G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=cuttlefish
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

# Run cuttlefish
cuttlefish build -d ../../../../2023_10_raw_data/data/complete_genomes/metadata -t 16 -o cuttlefish -f 1 -w ../../../../2023_10_raw_data/results/cuttlefish_result/

