#!/bin/bash

#sbatch details
#SBATCH --time=3:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=ppanggolin
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ppanggolin_combination/

# fasta files path
fasta_folder="/hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/combination_selected/"
# Output file path
output_file="/hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ppanggolin_combination/ppanggolin_input.tsv"

# Write fasta file names and paths to output file
find "$fasta_folder" -name "*.fasta" | while read -r filepath; do
    filename=$(basename -- "$filepath")
    filename_no_ext="${filename%.*}"  # Remove extension
    echo -e "$filename_no_ext\t$filepath" >> "$output_file"
done

echo "Input file list generated in $output_file"


ppanggolin all --fasta /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ppanggolin_combination/ppanggolin_input.tsv -o /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ppanggolin_combination/result -c 16
