#!/usr/bin/env bash

# ---------------------------
# Parse command-line arguments
# ---------------------------

while getopts "i:o:" opt; do
  case $opt in
    i) INPUT_DIR="$OPTARG" ;;
    o) OUTPUT_DIR="$OPTARG" ;;
    *) echo "Usage: $0 -i input_dir -o output_dir"; exit 1 ;;
  esac
done

# ---------------------------
# Validate arguments
# ---------------------------

if [[ -z "$INPUT_DIR" || -z "$OUTPUT_DIR" ]]; then
  echo "Error: both -i (input) and -o (output) directories are required."
  echo "Usage: $0 -i input_dir -o output_dir"
  exit 1
fi

if [[ ! -d "$INPUT_DIR" ]]; then
  echo "Error: input directory does not exist: $INPUT_DIR"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

# ---------------------------
# Process files
# ---------------------------

for f in "$INPUT_DIR"/*.fna; do
    [[ -e "$f" ]] || continue   # skip if no .fasta files exist

    filename=$(basename "$f")
    
    # Remove the suffix "_complete_genome.fna" (adjust if needed)
    clean_base="${filename%_complete_genome.fna}"


    awk -v base="$clean_base" -v outdir="$OUTPUT_DIR" '
        BEGIN {
            IGNORECASE=1
            plasmid_index=0
            current_out=""
        }

        /^>/ {
            # Is this a chromosome sequence?
            if ($0 ~ /chromosome/) {
                current_out=""   # skip chromosome
            } else {
                plasmid_index++
                current_out = outdir "/" base "_plasmid_" plasmid_index ".fasta"
                print $0 > current_out
            }
            next
        }

        # Print sequence lines only if we are inside a plasmid
        current_out != "" {
            print $0 > current_out
        }
    ' "$f"
done

echo "Finished extracting plasmids into: $OUTPUT_DIR"

