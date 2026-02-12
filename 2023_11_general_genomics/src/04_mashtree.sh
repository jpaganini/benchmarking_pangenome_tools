#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=32G
#SBATCH -c 8
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=mashtree
#SBATCH --error=logs/mashtree_%j.err
#SBATCH --output=logs/mashtree_%j.out

#Pass the miniconda3 installation directory and activate the right environment.

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate mashtree

#mashtree --numcpus 8 --tempdir ../results/mashtree/tmpdir --outmatrix ../results/mashtree/all_refseq_ecoli_matrix.tsv --outtree ../results/mashtree/all_refseq_ecoli.nwk --sort-order random --save-sketches ../results/mashtree/sketch ../../2023_10_raw_data/data/complete_genomes/ecoli/*fna

#tmp script, due to error beofore. Remove later
mashtree --numcpus 8 --tempdir ../results/mashtree/tmpdir --outmatrix ../results/mashtree/all_refseq_ecoli_matrix.tsv --outtree ../results/mashtree/all_refseq_ecoli.nwk --sort-order random ../results/mashtree/sketch/*msh

