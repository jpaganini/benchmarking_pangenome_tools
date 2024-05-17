#!/bin/bash

#sbatch details
#SBATCH --time=48:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=select_genomes
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

cd /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/long_read_selection/

./selection.sh -i /hpc/uu_vet_iras/pliu/remove_bad_result/panaroo_assembly_result/gene_presence_absence.Rtab -c 2 -t 16 -o short_reads_assembly_2
