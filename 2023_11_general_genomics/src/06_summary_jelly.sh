#!/usr/bin/env bash
set -euo pipefail

STATDIR="../results/jellyfish/stats"
OUT="../results/jellyfish/jellyfish_repeat_summary_k21.tsv"

mkdir -p "$(dirname "$OUT")"

echo -e "genome\tUnique\tDistinct\tTotal\tMax_count\trep_types\trep_frac_distinct\trep_frac_total" > "$OUT"

for f in "${STATDIR}"/*.txt; do
    [ -e "$f" ] || { echo "No stats files found in $STATDIR"; exit 1; }

    base=$(basename "$f" .txt)   # e.g. GCF_000978845.2_ASM97884v2

    Unique=$(awk '/^Unique:/   {print $2}' "$f")
    Distinct=$(awk '/^Distinct:/ {print $2}' "$f")
    Total=$(awk '/^Total:/    {print $2}' "$f")
    Max_count=$(awk '/^Max_count:/ {print $2}' "$f")

    # Number of repeated k-mer types
    rep_types=$((Distinct - Unique))

    # Fractions (floating point) using awk
    rep_frac_distinct=$(awk -v u="$Unique" -v d="$Distinct" 'BEGIN {printf "%.6f", (d-u)/d}')
    rep_frac_total=$(awk -v u="$Unique" -v t="$Total"    'BEGIN {printf "%.6f", (t-u)/t}')

    echo -e "${base}\t${Unique}\t${Distinct}\t${Total}\t${Max_count}\t${rep_types}\t${rep_frac_distinct}\t${rep_frac_total}" >> "$OUT"
done

echo "Written summary to: $OUT"

