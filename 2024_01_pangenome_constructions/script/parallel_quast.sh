#!/bin/bash

#1. mk directory to hold unicycler assemblies
mkdir /hpc/uu_vet_iras/pliu/parallel_quast_result

cd /hpc/uu_vet_iras/pliu/unicycler_assemblies

#2. get a list of the files
files=$(ls -1 | sort -u)

#create folder for temporary slurm scripts
mkdir /hpc/uu_vet_iras/pliu/quast_slurm_jobs

#create slurm scripts
for strains in $files
do
echo "#! /bin/bash
mkdir /hpc/uu_vet_iras/pliu/parallel_quast_result/${strains}
python /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/envs/panaroo/envs/QUAST/bin/quast --output-dir /hpc/uu_vet_iras/pliu/parallel_quast_result/${strains} -r /hpc/uu_vet_iras/pliu/complete_genome_adjust_name/complete_genome_adjust_name/${strains}_complete_genome.fna /hpc/uu_vet_iras/pliu/unicycler_assemblies/${strains}/assembly.fasta" > /hpc/uu_vet_iras/pliu/quast_slurm_jobs/${strains}.sh
done

#Run the scripts
cd /hpc/uu_vet_iras/pliu/quast_slurm_jobs
jobs=$(ls)
for slurm in $jobs
do
sbatch --time=8:00:00 --mem=30G ${slurm}
done
