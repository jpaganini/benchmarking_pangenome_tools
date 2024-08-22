# benchmarking_pangenome_tools

-Find reads of STEC E. coli at: /hpc/uu_vet_iras/jpaganini/data/benchmark_pangenome_graphs/2023_10_raw_data/data/sra_files/stec

-Find corresponding complete genomes at: /hpc/uu_vet_iras/jpaganini/data/benchmark_pangenome_graphs/2023_10_raw_data/data/complete_genomes/stec

IMPORTANT:
You will see that names between reads and complete genomes differ (Despite the fact that they belong to the same sample). Find the relations between these names in this git repo, in the file: 

benchmark_pangenome_graphs/2023_10_raw_data/results/stec_info/biosamples_strains_o157_h7.txt. 

Here: 1st column is the fastq-name and 3rd column is the corresponding fasta-name. Using this file you could change the names of the fastq-files to match complete-genomes (if you prefer!). 

BE CAREFUL! BECAUSE READS TAKE ONE DAY TO DOWNLOAD.

-Find more metadata of the genomes in the following repo: benchmark_pangenome_graphs/2023_10_raw_data/data/complete_genomes/metadata

-Find a list of potential steps to follow in this repo at: benchmark_pangenome_graphs/2023_10_raw_data/steps.txt


# Pangenome graph plot
1. The files for storing the pangenome graph are stored at the following link:
https://zenodo.org/records/13345365
2. The node length information in the cuttlefish graph is stored in the following link:
https://zenodo.org/records/13351559
The files in these two links (1,2) should be downloaded in the following directory: 
2024_8_pangenome_benchmark/source_data/pangenome_analysis_and_plot

3. The stx gene in ggcaller panaroo, ppanggolin is stored in the following link:
https://zenodo.org/records/13363371
The files in this link should be download in the following directory:


