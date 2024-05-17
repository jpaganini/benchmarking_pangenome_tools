#!/bin/bash

#sbatch details
#SBATCH --time=3:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=bifrost
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_7_bifrost_colored/biforst_complete

# Fasta files path
fasta_folder="/hpc/uu_vet_iras/pliu/remove_bad_result/complete_genome_remove_bad/"

# Output file path
output_file="/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_7_bifrost_colored/biforst_complete/bifrost_input.tsv"

# Write fasta file path to output file
find "$fasta_folder" -name "*.fna" > "$output_file"

echo "Input file list generated in $output_file"


Bifrost build -t 16 -k 31 -c -s /hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_7_bifrost_colored/biforst_complete/bifrost_input.tsv -o /hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_7_bifrost_colored/biforst_complete/biforst_complete



