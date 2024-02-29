#!/bin/bash

#sbatch details
#SBATCH --time=3:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=ppanggolin
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

# Run ppanggolin
ppanggolin workflow --anno ../../2023_10_raw_data/results/ppanggolin_input/ppanggolin_input.tsv -o ../../2023_10_raw_data/results/ppanggolin_result -c 16

# Unzip ppanggolin Result
gzip -d ../../2023_10_raw_data/results/ppanggolin_result/pangenomeGraph.gexf.gz

