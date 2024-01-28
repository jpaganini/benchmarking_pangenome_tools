#!/bin/bash

# Slurm details
#SBATCH --time=24:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=ppanggolin_input
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir ../../2023_10_raw_data/results/ppanggolin_input

# gff files path
gff_folder="../../2023_10_raw_data/results/ppanggolin_input"

for i in ../../2023_10_raw_data/results/bakta_result/*; do cp $i/*.gff3 ../../2023_10_raw_data/results/ppanggolin_input; done

# Output file path
output_file="../../2023_10_raw_data/results/ppanggolin_result/ppanggolin_input.tsv"

# Write gff file names and paths to output file
find "$gff_folder" -name "*.gff" | while read -r filepath; do
    filename=$(basename -- "$filepath")
    filename_no_ext="${filename%.*}"  # Remove extension
    echo -e "$filename_no_ext\t$filepath" >> "$output_file"
done

echo "Input file list generated in $output_file"

