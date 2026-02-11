#!/bin/bash

#1. mk directory to hold unicycler assemblies
mkdir /hpc/uu_vet_iras/pliu/unicycler_assemblies

cd /hpc/uu_vet_iras/pliu/unicycler_input

#2. get a list of the files
files=$(ls -1 | sed 's/_1.fastq//g' | sed 's/_2.fastq//g' | sort -u)

#create folder for temporary slurm scripts
mkdir /hpc/uu_vet_iras/pliu/unicycler_slurm_jobs

#create slurm scripts
for strains in $files
do
echo "#! /bin/bash
cd /hpc/uu_vet_iras/pliu/unicycler_input
unicycler -1 ${strains}_1.fastq -2 ${strains}_2.fastq -t 16 -o /hpc/uu_vet_iras/pliu/unicycler_assemblies/${strains}" > /hpc/uu_vet_iras/pliu/unicycler_slurm_jobs/${strains}.sh
done

#Run the scripts
cd /hpc/uu_vet_iras/pliu/unicycler_slurm_jobs
jobs=$(ls)
for slurm in $jobs
do
sbatch --time=20:00:00 --mem=30G ${slurm}
done
