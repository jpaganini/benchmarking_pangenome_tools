#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=128G
#SBATCH -c 8
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=mge
#SBATCH --error=logs/mge_%j.err
#SBATCH --output=logs/mge_%j.out

#Pass the miniconda3 installation directory and activate the right environment.

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate mge_cluster

mge_cluster --existing --input ../results/plasmid_analysis/mge_cluster/mge_input.txt --model_prefix ecoli --model_folder ../data/mge_cluster_ecoli --prefix STEC --outdir ../results/plasmid_analysis/mge_cluster


