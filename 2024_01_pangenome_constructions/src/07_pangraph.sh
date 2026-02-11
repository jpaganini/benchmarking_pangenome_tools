#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=p.liu1@students.uu.nl
#SBATCH --job-name=pangraph
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

#Should be ran under /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/pangraph

mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/pangraph_combination

cd /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/pangraph

julia --project=. src/PanGraph.jl build --circular /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/combination_selected/*.fasta > /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/pangraph_combination/ecoli_pangraph.json

julia --project=. src/PanGraph.jl export --no-duplications --output-directory /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/pangraph_combination /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/pangraph_combination/ecoli_pangraph.json


