#!/usr/bin/env python3
import argparse
import csv
import json
from collections import defaultdict


def parse_args():
    p = argparse.ArgumentParser(
        description=(
            "Generate block × strain abundance for missing blocks only, "
            "using pangraph JSON paths and a replicon→strain mapping."
        )
    )
    p.add_argument(
        "--missing-blocks",
        required=True,
        help="TXT file with one missing block ID per line."
    )
    p.add_argument(
        "--json",
        required=True,
        help="pangraph graph.json (must contain paths[].blocks[])."
    )
    p.add_argument(
        "--mapping",
        required=True,
        help="TSV: strain_id<TAB>replicon_id"
    )
    p.add_argument(
        "--output",
        required=True,
        help="Output CSV (block × strain matrix)."
    )
    p.add_argument(
        "--mapping-has-header",
        action="store_true",
        help="Set if mapping TSV has a header line."
    )
    return p.parse_args()


def load_missing_blocks(path):
    blocks = set()
    with open(path) as f:
        for line in f:
            bid = line.strip()
            if bid:
                blocks.add(bid)
    return blocks


def parse_mapping(mapping_path, has_header=False):
    """
    Returns:
        path_to_strain: dict {replicon_id: strain}
        strains: sorted list of strains
    """
    path_to_strain = {}
    strains = set()

    with open(mapping_path) as f:
        first = True
        for line in f:
            line = line.strip()
            if not line:
                continue
            if first and has_header:
                first = False
                continue

            parts = line.split("\t")
            if len(parts) < 2:
                continue
            strain, replicon = parts[0], parts[1]

            path_to_strain[replicon] = strain
            strains.add(strain)

    return path_to_strain, sorted(strains)


def main():
    args = parse_args()

    missing_blocks = load_missing_blocks(args.missing_blocks)
    path_to_strain, strains = parse_mapping(
        args.mapping, args.mapping_has_header
    )
    n_total_strains = len(strains)

    # block -> strain -> count
    block_strain_abundance = defaultdict(lambda: defaultdict(int))
    block_total_occ = defaultdict(int)

    # Load JSON
    with open(args.json) as f:
        graph = json.load(f)

    paths = graph.get("paths", [])

    for path in paths:
        replicon = str(path.get("name", ""))
        if not replicon:
            continue

        # Only consider replicons that map to a strain
        if replicon not in path_to_strain:
            continue

        strain = path_to_strain[replicon]

        for b in path.get("blocks", []):
            bid = b.get("id")
            if bid in missing_blocks:
                block_strain_abundance[bid][strain] += 1
                block_total_occ[bid] += 1

    # Write output
    with open(args.output, "w", newline="") as out_f:
        w = csv.writer(out_f)

        header = [
            "block_id",
            "total_occurrences",
            "n_strains",
            "frac_strains",
        ] + strains
        w.writerow(header)

        for bid in sorted(missing_blocks):
            per_strain = block_strain_abundance.get(bid, {})
            n_strains_present = sum(
                1 for s in strains if per_strain.get(s, 0) > 0
            )
            frac = (
                n_strains_present / n_total_strains
                if n_total_strains > 0 else 0.0
            )

            row = [
                bid,
                block_total_occ.get(bid, 0),
                n_strains_present,
                f"{frac:.6f}",
            ]
            for s in strains:
                row.append(per_strain.get(s, 0))

            w.writerow(row)


if __name__ == "__main__":
    main()
