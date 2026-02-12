#!/bin/bash

#sbatch details
#SBATCH --time=48:00:00
#SBATCH --mem=16G
#SBATCH -c 8
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=download_stec_reads
#SBATCH --error=slurm-%j_ectyper.err
#SBATCH --output=slurm-%j_ectyper.out

source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate sra_tools

#1. Get the strains that have an O157:H7 serotype - THIS HAS TO BE FIXED
grep 'O157:H7' ../results/ectyper/output.tsv | cut -f 1 | sed 's/_genomic//g' >> ../results/stec_info/strains_O157_h7.txt
stx_isolates=$(cat ../results/stec_info/strains_O157_h7.txt)
for isolate in $stx_isolates ; do biosample=$(grep ${isolate} ../data/complete_genomes/metadata/ecoli_metadata.tsv | cut -f 3); echo ${biosample},${isolate} >> ../results/stec_info/biosample_strains_o157_h7.csv; done

stx_biosamples=$(cat ../results/stec_info/biosample_strains_o157_h7.csv | cut -f 1 -d ,)
for biosample in $stx_biosamples ; do grep ${biosample} ../data/complete_genomes/metadata/ecoli_sra_reads.csv | cut -f 2 -d , >> ../results/stec_info/all_sra_0157_h7.txt ; done

#1. Get a list of sra_ids 
sra_accessions=$(cat ../results/stec_info/all_sra_0157_h7.txt | cut -f 1 -d ' ')

#2. Make a directory for holding the results
mkdir ../data/sra_files/stec

#3. Make a loop to download the srr files
for reads in $sra_accessions
do
fasterq-dump --split-files ${reads} -O ../data/sra_files/stec   
done

#Add all info together
for biosample in $stx_biosamples ; do reads=$(grep ${biosample} ../data/complete_genomes/metadata/ecoli_sra_reads.csv | cut -f 2 -d , | cut -f 1 -d ' '); if [ -n "$reads" ]; then sed -i "s/${biosample}/${reads},${biosample}/g" ../results/stec_info/biosample_strains_o157_h7.csv; else sed -i "s/${biosample}/no_reads,${biosample}/g" ../results/stec_info/biosample_strains_o157_h7.csv; fi;  done

#Separate genomes
available_ecoli_reads=$(ls ../data/sra_files/stec/ | sed 's/_1.fastq//g' | sed 's/_2.fastq//g' | sort -u )
for reads in ${available_ecoli_reads}; do isolate=$(grep ${reads} ../results/stec_info/biosample_strains_o157_h7.csv | cut -f 3 -d , ); cp ../data/complete_genomes/ecoli/${isolate}_genomic.fna ../data/complete_genomes/stec/; done
