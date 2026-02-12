#!/bin/bash

# sbatch details
#SBATCH --time=24:00:00
#SBATCH --mem=32G
#SBATCH -c 8
#SBATCH --mail-type=all
#SBATCH --mail-user=j.a.paganini@uu.nl
#SBATCH --job-name=jelly
#SBATCH --error=logs/jelly_%j.err
#SBATCH --output=logs/jelly_%j.out

# Load conda and activate environment
source ~/data/miniconda3/etc/profile.d/conda.sh
conda activate jellyfish

set -euo pipefail

# PARAMETERS
K=21                 # k-mer size; set to 31 if you want
THREADS=8            # match SBATCH -c 8

INDIR="/home/uu_vet_iras/jpaganini/data/benchmarking_pangenome_tools/2023_10_raw_data/data/complete_genomes/ecoli"
JFDIR="/home/uu_vet_iras/jpaganini/data/benchmarking_pangenome_tools/2023_11_general_genomics/results/jellyfish/dbs"
STATDIR="/home/uu_vet_iras/jpaganini/data/benchmarking_pangenome_tools/2023_11_general_genomics/results/jellyfish/stats"

mkdir -p "$JFDIR" "$STATDIR"

echo "Running jellyfish count + stats for all genomes in: $INDIR"
echo "k = $K, threads = $THREADS"
echo

# Make globs that don’t match expand to nothing instead of a literal string
shopt -s nullglob

# Collect matching fasta files
files=( "${INDIR}"/GC*_genomic.fna )

if [[ ${#files[@]} -eq 0 ]]; then
    echo "ERROR: No GCF_*_genomic.fna files found in $INDIR"
    exit 1
fi

echo "Found ${#files[@]} genomes:"
printf '  %s\n' "${files[@]:0:5}"
[[ ${#files[@]} -gt 5 ]] && echo "  ..."

for fa in "${files[@]}"; do
    base=$(basename "$fa" _genomic.fna)          # e.g. GCF_000978845.2_ASM97884v2
    jf="${JFDIR}/${base}.jf"
    stats="${STATDIR}/${base}.txt"

    echo ">>> Processing $base"

    if [[ ! -s "$jf" ]]; then
        echo "    - Counting kmers -> $jf"
        jellyfish count \
            -m "$K" \
            -s 100M \
            -t "$THREADS" \
            -C \
            -o "$jf" \
            "$fa"
    else
        echo "    - Skipping count (already exists and non-empty)"
    fi

    echo "    - Computing stats -> $stats"
    jellyfish stats -o "$stats" "$jf"
done

echo
echo "Done. Jellyfish DBs in:   $JFDIR"
echo "Stats files in:           $STATDIR"

