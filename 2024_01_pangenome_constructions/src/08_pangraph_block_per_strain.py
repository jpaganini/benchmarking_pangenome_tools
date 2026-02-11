#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Create a block × strain presence/abundance matrix from a pangraph GFA "
            "and a replicon→strain mapping file."
        )
    )
    parser.add_argument(
        "--gfa",
        required=True,
        help="Input pangraph GFA file (with S and P lines).",
    )
    parser.add_argument(
        "--mapping",
        required=True,
        help=(
            "Replicon-to-strain mapping TSV file. "
            "Two columns: strain_id<TAB>replicon_id (no header by default)."
        ),
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output CSV file for block × strain matrix.",
    )
    parser.add_argument(
        "--missing-blocks",
        required=True,
        help="Output TXT file listing block IDs present in S but absent from all P paths.",
    )
    parser.add_argument(
        "--mapping-has-header",
        action="store_true",
        help="Set this if the mapping file has a header line to skip.",
    )
    return parser.parse_args()


def parse_gfa(gfa_path):
    """
    Parse pangraph GFA file.

    Returns:
        block_lengths: dict {block_id: length}
        path_blocks:   dict {path_id: set(block_id, ...)}
        blocks_in_S:   set(block_id) observed in S lines
        blocks_in_P:   set(block_id) observed in P lines
    """
    block_lengths = {}
    path_blocks = defaultdict(set)
    blocks_in_S = set()
    blocks_in_P = set()

    with open(gfa_path) as f:
        for line in f:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("\t")
            rec_type = fields[0]

            # S lines: segments = pancontigs / blocks
            if rec_type == "S":
                # S <block_id> * LN:i:<len> ...
                block_id = fields[1]
                blocks_in_S.add(block_id)

                length = None
                for tag in fields[3:]:
                    # Look for LN:i:<value>
                    if tag.startswith("LN:i:"):
                        try:
                            length = int(tag.split(":", 2)[2])
                        except ValueError:
                            pass
                        break
                block_lengths[block_id] = length

            # P lines: paths (replicons or contigs)
            elif rec_type == "P":
                # P <path_id> <segments> <overlaps...>
                if len(fields) < 3:
                    continue
                path_id = fields[1]
                segs_field = fields[2]
                segments = segs_field.split(",")

                for seg in segments:
                    seg = seg.strip()
                    if not seg:
                        continue
                    # remove trailing + or - to get block_id
                    if seg[-1] in "+-":
                        block_id = seg[:-1]
                    else:
                        block_id = seg

                    path_blocks[path_id].add(block_id)
                    blocks_in_P.add(block_id)

    return block_lengths, path_blocks, blocks_in_S, blocks_in_P


def parse_mapping(mapping_path, has_header=False):
    """
    Parse replicon-to-strain mapping.

    Assumes TSV with at least two columns:
        strain_id<TAB>replicon_id

    Returns:
        strain_to_paths: dict {strain: set(path_id, ...)}
        path_to_strain: dict {path_id: strain}
    """
    strain_to_paths = defaultdict(set)
    path_to_strain = {}

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

            # We assume replicon == path_id in the GFA P lines.
            path_id = replicon

            strain_to_paths[strain].add(path_id)
            path_to_strain.setdefault(path_id, strain)

    return strain_to_paths, path_to_strain


def main():
    args = parse_args()

    # 1) Parse GFA
    block_lengths, path_blocks, blocks_in_S, blocks_in_P = parse_gfa(args.gfa)

    # 2) Parse mapping
    strain_to_paths, path_to_strain = parse_mapping(
        args.mapping, has_header=args.mapping_has_header
    )

    # Write missing blocks (S but not in any P)
    missing_blocks = sorted(blocks_in_S - blocks_in_P)
    with open(args.missing_blocks, "w") as mh:
        for bid in missing_blocks:
            mh.write(f"{bid}\n")

    # Set of all strains
    strains = sorted(strain_to_paths.keys())
    n_total_strains = len(strains)

    # 3) Build block → strain abundance from P lines only
    block_strain_abundance = defaultdict(lambda: defaultdict(int))
    block_total_occurrences = defaultdict(int)

    for path_id, blocks in path_blocks.items():
        if path_id not in path_to_strain:
            continue
        strain = path_to_strain[path_id]

        for block_id in blocks:
            block_strain_abundance[block_id][strain] += 1
            block_total_occurrences[block_id] += 1

    # 4) Write matrix
    with open(args.output, "w", newline="") as out_f:
        writer = csv.writer(out_f)

        header = ["block_id", "length", "total_occurrences", "n_strains", "frac_strains"]
        header.extend(strains)
        writer.writerow(header)

        for block_id in sorted(block_strain_abundance.keys()):
            length = block_lengths.get(block_id)
            total_occ = block_total_occurrences.get(block_id, 0)

            strains_with_block = [
                s for s in strains if block_strain_abundance[block_id].get(s, 0) > 0
            ]
            n_strains = len(strains_with_block)
            frac_strains = n_strains / n_total_strains if n_total_strains > 0 else 0.0

            row = [
                block_id,
                length if length is not None else "",
                total_occ,
                n_strains,
                f"{frac_strains:.6f}",
            ]

            for s in strains:
                row.append(block_strain_abundance[block_id].get(s, 0))

            writer.writerow(row)


if __name__ == "__main__":
    main()
