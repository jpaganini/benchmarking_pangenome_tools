import pandas as pd

# Read the CSV file
df = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/merged_virulencefinder_blast_bakta_panaroo.csv")

# Step 1: Remove the part between 'stx' and '_' in the Stx_type column
df['Stx_type'] = df['Stx_type'].str.replace(r'stx[^_]*_', 'stx_', regex=True)

# Step 2: Delete the 'Accession_number' and 'Stx_gene' columns
df = df.drop(columns=['Accession_number', 'Stx_gene'])

# Fill NaN values with 0
df.fillna(0, inplace=True)

# Perform aggregation on each group: sum numeric columns and take the maximum of non-numeric columns
df = df.groupby(['Isolate', 'Stx_type']).agg(
    lambda x: x.sum() if pd.api.types.is_numeric_dtype(x) else x.max()
).reset_index()

# Output the modified DataFrame
print(df)

# Save the modified result to a new CSV file
df.to_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/merged_virulencefinder_blast_bakta_panaroo_remove_type.csv", index=False)
