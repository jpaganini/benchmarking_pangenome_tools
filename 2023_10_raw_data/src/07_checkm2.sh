#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=checkm2
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir /hpc/uu_vet_iras/pliu/checkm2_result

checkm2 predict --threads 16 --input /hpc/uu_vet_iras/pliu/unicycler_assemblies_adjust_name -x .fasta --output-directory /hpc/uu_vet_iras/pliu/checkm2_result 
