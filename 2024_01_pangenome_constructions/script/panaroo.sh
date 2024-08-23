#!/bin/bash


#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=panaroo
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/panaroo_combination

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/panaroo_combination/panaroo_combination_input

cd /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/assembly_bakta

for i in *;do cp $i/*.gff3 /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/panaroo_combination/panaroo_combination_input;done

cd /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/complete_bakta

for i in *;do cp $i/*.gff3 /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/panaroo_combination/panaroo_combination_input;done

panaroo -i /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/panaroo_combination/panaroo_combination_input/*.gff3 -o /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/panaroo_combination -t 16 --clean-mode strict --remove-invalid-genes
