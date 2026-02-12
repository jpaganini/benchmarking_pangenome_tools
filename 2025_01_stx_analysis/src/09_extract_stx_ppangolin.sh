#!/bin/bash

#REQUIRES FIXING!

conda activate pangolin
ppanggolin fasta -p pangenome.h5 --output MY_GENES_FAMILIES --gene_families all
cd MY_GENE_FAMILIES
mkdir stx_blast_output
conda activate blast
blastn -db /hpc/uu_vet_iras/pliu/remove_bad_result/blast_all_stx_genes/database/stx -query all_nucleotide_families.fasta -out stx_blast_output/stx_all_99.csv -perc_identity 99 -qcov_hsp_perc 0.8 -outfmt "6 qseqid sseqid qstart qend sstart ssend evalue length pident qcovs mismatch gaps"
cd stx_blast_output
cut -f 1 stx_all_99.csv | sort -u >> ../stx_gene_families.txt
cd ..
stx_genes=$(cat stx_gene_families.txt)
cd ..
head -n 1 gene_presence_absence.Rtab >> stx_presence_absence.tsv
for code in $stx_genes; do grep ${code} gene_presence_absence.Rtab >> stx_presence_absence.tsv; done
