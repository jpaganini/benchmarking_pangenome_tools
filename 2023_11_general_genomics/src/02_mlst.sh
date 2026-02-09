#!/bin/bash

#sbatch details
#SBATCH --time=48:00:00
#SBATCH --mem=16G
#SBATCH -c 8
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=mlst
#SBATCH --error=logs/mlst_%j.err
#SBATCH --output=logs/mlst_%j.out

#Pass the miniconda3 installation directory and activate the right environment.

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate mlst

mlst --scheme ecoli_achtman_4 ../../2023_10_raw_data/data/complete_genomes/ecoli/*fna > ../results/all_mlst.tsv        

