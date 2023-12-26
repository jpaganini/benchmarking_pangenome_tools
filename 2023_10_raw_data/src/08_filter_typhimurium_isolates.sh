#!/bin/bash


mkdir -p ../results/typhimurium_info

#1. Create a file with a list of isolates of S> typhimurium (n=297)
cat ../results/sistr/modified_output/*csv | cut -f 8,15 -d , | grep Typhimurium >> ../results/typhimurium_info/strains_typhimurium.csv

#2. Create a file with a list of biosamples
typhimurium_isolates=$(cut -f 1 -d , ../results/typhimurium_info/strains_typhimurium.csv)
for things in $typhimurium_isolates ; do grep ${things} ../data/complete_genomes/metadata/senterica_metadata.tsv; done | cut -f 3
>> ../results/typhimurium_info/biosample_typhimurium.txt

#3. Filter the reads

