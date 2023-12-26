#!/bin/bash

#sbatch details
#SBATCH --time=48:00:00
#SBATCH --mem=16G
#SBATCH -c 8
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=download_typhimurium_reads
#SBATCH --error=slurm-%j_sra_typhimurium.err
#SBATCH --output=slurm-%j_sra_typhimurium.out

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate sra_tools

#1. Get a list of sra_ids 
sra_accessions=$(cat ../results/typhimurium_info/sra_codes_typhimurium.txt | cut -f 1 -d ' ')

#2. Make a directory for holding the results
mkdir ../data/sra_files/typhimurium

#3. Make a loop to download the sra files
for reads in $sra_accessions
do
fasterq-dump --split-files ${reads} -O ../data/sra_files/typhimurium   
done
