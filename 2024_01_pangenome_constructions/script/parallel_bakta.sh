#!/bin/bash

#1. mk directory to hold unicycler assemblies
mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/assembly_bakta

cd /hpc/uu_vet_iras/pliu/unicycler_assemblies

#2. get a list of the files
files=$(ls -1 | sort -u)

#create folder for temporary slurm scripts
mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/bakta_assembly_slurm_jobs

#create slurm scripts
for strains in $files
do
echo "#! /bin/bash
bakta --db /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/db --output /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/assembly_bakta/${strains} /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/combination_selected/${strains}_assembly.fasta" > /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/bakta_assembly_slurm_jobs/${strains}.sh
done

#Run the scripts
cd /hpc/uu_vet_iras/pliu/remove_bad_result/combination_2_assembly/bakta_assembly_slurm_jobs
jobs=$(ls)
for slurm in $jobs
do
sbatch --time=16:00:00 --mem=30G ${slurm}
done
