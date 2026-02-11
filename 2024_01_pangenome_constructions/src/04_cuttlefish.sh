#!/bin/bash

#sbatch details
#SBATCH --time=72:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=cuttlefish1
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/cuttlefish_complete_genome_2

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/cuttlefish_complete_genome_2/cuttlefish_combination_input

cd /hpc/uu_vet_iras/pliu/remove_bad_result/complete_genome_remove_bad/

cp *.fna /hpc/uu_vet_iras/pliu/remove_bad_result/cuttlefish_complete_genome_2/cuttlefish_combination_input

cd /hpc/uu_vet_iras/pliu/remove_bad_result/cuttlefish_complete_genome_2

# Run cuttlefish
cuttlefish build -d /hpc/uu_vet_iras/pliu/remove_bad_result/cuttlefish_complete_genome_2/cuttlefish_combination_input -t 16 -o cuttlefish_complete_2 -k 31 -f 1 -w /hpc/uu_vet_iras/pliu/remove_bad_result/cuttlefish_complete_genome_2

