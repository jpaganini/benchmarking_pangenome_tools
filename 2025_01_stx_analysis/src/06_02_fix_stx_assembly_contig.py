import pandas as pd

# Read the CSV file
df = pd.read_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/uniformed_stx_assembly_contig_number.csv')

# Extract the substring between '_lcl|' and '.1_' from the 'Stx_gene' column
df['Accession_number'] = df['Stx_gene'].str.extract(r'_lcl\|(.*?)\.1_')

# Save the result to a new CSV file
df.to_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/update_uniformed_stx_assembly_contig_number.csv', index=False)
