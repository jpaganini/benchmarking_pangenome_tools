#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=bifrost_input
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

# Fasta files path
fasta_folder="../../2023_10_raw_data/data/complete_genomes/metadata"

# Output file path 
output_file="../../2023_10_raw_data/results/bifrost_result/bifrost_input.txt"

# Write fasta file path to output file 
find "$fasta_folder" -name "*.fna" > "$output_file"

echo "Input file list generated in $output_file"


