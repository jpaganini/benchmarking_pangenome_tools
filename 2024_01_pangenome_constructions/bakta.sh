#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=20G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=bakta
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out


# Create input and output files directory
input_dir="../../2023_10_raw_data/data/complete_genomes/metadata"
output_dir="../../2023_10_raw_data/results/bakta_result"

cd ../2023_10_raw_data/results
# Write input files list
for fna_file in *.fna; do
    # get file name
    base_name=$(basename "$fna_file" .fna)

    # create out put path
    output_subdir="$output_dir/$base_name"

    # bakta
    bakta --db ../2023_10_raw_data/data/complete_genomes/db --output "$output_subdir" --prefix $base_name --threads 16 $fna_file
done
