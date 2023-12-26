#!/bin/bash

#sbatch details
#SBATCH --time=48:00:00
#SBATCH --mem=16G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=senterica_serotyping
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

#Pass the miniconda3 installation directory and activate the right environment.

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate sistr

#create a directory to hold the results
mkdir ../results/sistr

#get a list of isolates
isolate_names=$(ls -h ../data/complete_genomes/senterica/*fna | xargs -n 1 basename | sed "s/_genomic.fna//g")

#Loop thru the files and run sistr
for isolate in $isolate_names
do
sistr -i ../data/complete_genomes/senterica/${isolate}_genomic.fna ${isolate} -o ../results/sistr/${isolate} -f csv -t 16
done
