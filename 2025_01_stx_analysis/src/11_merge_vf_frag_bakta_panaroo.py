import pandas as pd

# Read all CSV files
df1 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/uniformed_duplicate_virulencefinder_complete.csv")
df2 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/update_uniformed_stx_assembly_contig_number.csv")
df3 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/uniformed_bakta_assembly_annotaion.csv")
df4 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/uniformed_bakta_complete_annotaion.csv")
df5 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_assembly_stx.csv")
df6 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_1%_complete_stx.csv")
df7 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_10%_complete_stx.csv")
df8 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_50%_complete_stx.csv")
df9 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_90%_complete_stx.csv")
df10 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_99%_complete_stx.csv")
df11 = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_complete_stx.csv")

# Merge DataFrames
merged_df = pd.merge(df1, df2, on=['Isolate', 'Stx_type', 'Accession_number'], how='outer')

for df in [df3, df4, df5, df6, df7, df8, df9, df10, df11]:
    merged_df = pd.merge(merged_df, df, on=['Isolate', 'Stx_type'], how='outer')

# Remove duplicate rows
merged_df = merged_df.drop_duplicates()

# Save the merged data to a CSV file
merged_df.to_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/merged_virulencefinder_blast_bakta_panaroo.csv", index=False)


