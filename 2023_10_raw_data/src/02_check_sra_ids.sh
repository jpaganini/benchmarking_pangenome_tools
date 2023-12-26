#!/bin/bash

#activate conda environtment
conda activate ed_utils

#1- Get the list of the biosamples Id to check if we have the reads that will later be used to run the alignments

biosamples=$(cat ../complete_genomes/ecoli/ecoli_biosamples.csv)

#2. Now, we will make a look to get the reads identifiers

for biosample in $biosamples
do
sra_accession=$(esearch -db biosample -query "${biosample}" | elink -target sra | efetch -format runinfo  | grep 'Illumina\|ILLUMINA' | cut -f 1 -d ,)
echo ${biosample},${sra_accession} >> ../complete_genomes/ecoli/available_sra_reads.csv
done


#COmpelte for Salmonella
