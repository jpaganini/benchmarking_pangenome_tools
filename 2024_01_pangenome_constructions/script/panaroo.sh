#!/bin/bash


#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=panaroo
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

# Make input file directory
mkdir ../../2023_10_raw_data/results/panaroo_input

# Copy gff3 files from bakta result to input file directory
for i in ../../2023_10_raw_data/results/bakta_result/*; do cp $i/*.gff3 ../../2023_10_raw_data/results/panaroo_input; done

# Run panaroo
panaroo -i ../../2023_10_raw_data/results/panaroo_input/*.gff3 -o ../../2023_10_raw_data/results/panaroo_result -t 16 --clean-mode strict --merge_paralogs --remove-invalid-genes 
