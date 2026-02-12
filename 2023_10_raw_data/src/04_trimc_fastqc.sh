#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=20G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=short_reads_qc
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out



input_dir="/hpc/uu_vet_iras/pliu/stec_short_reads"
output_dir="/hpc/uu_vet_iras/pliu/stec_short_reads_qc"

cd /hpc/uu_vet_iras/pliu/stec_short_reads

for fastq_file in *.fastq; do
    # get file name
    base_name=$(basename "$fastq_file" .fastq)

    mkdir hpc/uu_vet_iras/pliu/stec_short_reads_qc/"$base_name"

    # create out put path
    output_subdir="$output_dir/$base_name"

    # trim_galore
    trim_galore --quality 20 --fastqc --output_dir "$output_subdir" /hpc/uu_vet_iras/pliu/stec_short_reads/$fastq_file
done
