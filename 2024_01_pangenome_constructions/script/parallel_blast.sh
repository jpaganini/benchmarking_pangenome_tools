#!/bin/bash

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/result

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/blast_slurm_jobs

# Set the CSV file path
csv_file="/hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/stx_complete_results_deduplicate.csv"

# Read CSV file and create bash script files
while IFS=, read -r folder accession_number; do
    folder=$(echo "$folder" | sed 's/[^a-zA-Z0-9+]//g')
    accession_number=$(echo "$accession_number" | sed 's/[^a-zA-Z0-9+]//g')
    echo "#!/bin/bash
    blastn -db /hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/database/${accession_number} \
    -query /hpc/uu_vet_iras/pliu/remove_bad_result/assembly_remove_bad/${folder}_assembly.fasta \
    -out /hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/result/${folder}+${accession_number}.csv -perc_identity 99 -qcov_hsp_perc 10 -outfmt \"6 qseqid sseqid qstart qend sstart ssend evalue length pident qcovs mismatch gaps\"" \
    > "/hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/blast_slurm_jobs/${folder}+${accession_number}.sh"

    # Set execute permissions for the script file
    chmod +x "/hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/blast_slurm_jobs/${folder}+${accession_number}.sh"
done < "$csv_file"

# Run the scripts
cd /hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/blast_slurm_jobs
for slurm in *
do
    sbatch --time=16:00:00 --mem=30G "$slurm"
done