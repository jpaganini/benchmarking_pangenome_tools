#!/bin/bash

#sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=40G
#SBATCH -c 16
#SBATCH --gres=tmpspace:40G
#SBATCH --mail-type=all
#SBATCH --job-name=pangraph
#SBATCH --error=slurm-%j_sistr.err
#SBATCH --output=slurm-%j_sistr.out

cd /path/to/pangraph/direct

# Should be ran under /hpc/local/CentOS7/uu_vet_iras/pliu_anaconda/pangraph
julia --project=. src/PanGraph.jl build --circular ../../2023_10_raw_data/data/complete_genomes/metadata/*.fna > ../../2023_10_raw_data/results/pangraph_result/ecoli_pangraph.json

# Export gfa file
julia --project=. src/PanGraph.jl export --no-duplications --output-directory ../../2023_10_raw_data/results/pangraph_result ../../2023_10_raw_data/results/pangraph_result/ecoli_pangraph.json
