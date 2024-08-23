#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=60G
#SBATCH -c 16
#SBATCH --gres=tmpspace:60G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=ggcaller
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ggcaller_combination

ls -d -1 /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/combination_selected/*.fasta > /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ggcaller_combination/ggcaller_input.txt

ggcaller --refs /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ggcaller_combination/ggcaller_input.txt --out /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/ggcaller_combination --threads 16
