#!/usr/bin/env python3
import argparse
import gzip
import sys
import pandas as pd


def open_text(path):
    """Open plain text or gzipped text file transparently."""
    if path.endswith(".gz"):
        return gzip.open(path, "rt")
    return open(path, "r")


def load_gfa_mapping(gfa_path):
    """
    Parse a GFA file and return a dict:
        sequence (str) -> segment_id (str or ';'-joined if multiple).
    Only 'S' lines with an explicit sequence are used.
    """
    seq_to_id = {}

    with open_text(gfa_path) as fh:
        for line in fh:
            if not line or line[0] == "#":
                continue
            parts = line.rstrip("\n").split("\t")
            if parts[0] != "S":
                continue
            # GFA: S <segment_id> <sequence> ...
            if len(parts) < 3:
                continue
            seg_id = parts[1]
            seq = parts[2]

            # Some GFA variants use '*' for no sequence
            if seq == "*":
                continue

            # Handle possible duplicates: store all IDs, then join
            if seq in seq_to_id:
                existing = seq_to_id[seq]
                if isinstance(existing, list):
                    existing.append(seg_id)
                else:
                    seq_to_id[seq] = [existing, seg_id]
            else:
                seq_to_id[seq] = seg_id

    # Convert lists of multiple IDs to a single ';'-separated string
    for seq, val in list(seq_to_id.items()):
        if isinstance(val, list):
            seq_to_id[seq] = ";".join(val)

    return seq_to_id


def merge_rtab_with_gfa(rtab_path, gfa_mapping, out_path):
    """
    Read the .rtab file, add:
      - Segment_ID column using the GFA mapping
      - total_presence column (sum across sample columns)
      - presence_fraction column (total_presence / number_of_samples)
    and write the merged table.
    """
    # Read rtab (tab-separated, header present)
    df = pd.read_csv(rtab_path, sep="\t", dtype=str)

    if "Unitig_sequence" not in df.columns:
        sys.stderr.write("ERROR: 'Unitig_sequence' column not found in rtab file.\n")
        sys.exit(1)

    # Map unitig sequences to segment IDs
    df["Segment_ID"] = df["Unitig_sequence"].map(gfa_mapping)

    # Identify sample columns (everything except Unitig_sequence and Segment_ID)
    sample_cols = [c for c in df.columns if c not in ["Unitig_sequence", "Segment_ID"]]

    # Convert presence/absence to numeric and sum across rows
    df_numeric = df[sample_cols].apply(pd.to_numeric, errors="coerce").fillna(0)
    df["total_presence"] = df_numeric.sum(axis=1).astype(int)

    # Presence fraction = total_presence / number_of_samples
    n_samples = len(sample_cols)
    if n_samples == 0:
        sys.stderr.write("ERROR: No sample columns found in rtab file.\n")
        sys.exit(1)

    df["presence_fraction"] = df["total_presence"] / float(n_samples)

    # Write out TSV
    df.to_csv(out_path, sep="\t", index=False)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Merge an .rtab file with a GFA graph via unitig sequence.\n"
            "Adds 'Segment_ID', 'total_presence', and 'presence_fraction' columns."
        )
    )
    parser.add_argument(
        "--graph",
        required=True,
        help="Path to the GFA file (can be .gz).",
    )
    parser.add_argument(
        "--rtab",
        required=True,
        help="Path to the .rtab file with a 'Unitig_sequence' column.",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Path to write the merged output (.tsv).",
    )

    args = parser.parse_args()

    # Load mapping from GFA
    gfa_mapping = load_gfa_mapping(args.graph)

    # Merge and write out
    merge_rtab_with_gfa(args.rtab, gfa_mapping, args.out)


if __name__ == "__main__":
    main()
