#!/bin/bash

#1. go to directory which hold unicycler assemblies

cd /hpc/uu_vet_iras/pliu/unicycler_assemblies

#2. get a list of the files
files=$(ls -1 | sort -u)

#create folder for temporary slurm scripts
mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_assembly/virulencefinder_assembly_slurm_jobs

#create slurm scripts
for strains in $files
do
echo "#! /bin/bash 
mkdir /hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_assembly/${strains}
python /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/virulencefinder/virulencefinder.py -i /hpc/uu_vet_iras/pliu/remove_bad_result/assembly_remove_bad/${strains}_assembly.fasta -o /hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_assembly/${strains} -p /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/virulencefinder_db -mp /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/ncbi-blast-2.15.0+/bin/blastn -t 0.90 -x" > /hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_assembly/virulencefinder_assembly_slurm_jobs/${strains}.sh
done


#Run the scripts
cd /hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_assembly/virulencefinder_assembly_slurm_jobs
jobs=$(ls)
for slurm in $jobs
do
sbatch --time=16:00:00 --mem=30G ${slurm}
done
