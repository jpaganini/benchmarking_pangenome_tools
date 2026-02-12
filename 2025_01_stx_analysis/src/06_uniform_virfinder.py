import pandas as pd

# Read the CSV file
df = pd.read_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/stx_complete_virulencefinder_subunits.csv')

# Count the occurrences of each row and add this as a new column
df['No_of_stx_gene_virulencefinder'] = df.groupby(df.columns.tolist()).transform('size')

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the processed DataFrame to a new CSV file
df.to_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/uniformed_duplicate_virulencefinder_complete.csv', index=False)
