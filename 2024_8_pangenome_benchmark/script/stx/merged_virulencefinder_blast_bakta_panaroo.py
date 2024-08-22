import pandas as pd

# Read all CSV files
df1 = pd.read_csv("../../result/stx/uniformed_duplicate_virulencefinder_complete.csv")
df2 = pd.read_csv("../../result/stx/update_uniformed_stx_assembly_contig_number.csv")
df3 = pd.read_csv("../../result/stx/uniformed_bakta_assembly_annotaion.csv")
df4 = pd.read_csv("../../result/stx/uniformed_bakta_complete_annotaion.csv")
df5 = pd.read_csv("../../result/stx/panaroo_result/panaroo_assembly_stx.csv")
df6 = pd.read_csv("../../result/stx/panaroo_result/panaroo_1%_complete_stx.csv")
df7 = pd.read_csv("../../result/stx/panaroo_result/panaroo_10%_complete_stx.csv")
df8 = pd.read_csv("../../result/stx/panaroo_result/panaroo_50%_complete_stx.csv")
df9 = pd.read_csv("../../result/stx/panaroo_result/panaroo_90%_complete_stx.csv")
df10 = pd.read_csv("../../result/stx/panaroo_result/panaroo_99%_complete_stx.csv")
df11 = pd.read_csv("../../result/stx/panaroo_result/panaroo_complete_stx.csv")

# Merge DataFrames
merged_df = pd.merge(df1, df2, on=['Isolate', 'Stx_type', 'Accession_number'], how='outer')

for df in [df3, df4, df5, df6, df7, df8, df9, df10, df11]:
    merged_df = pd.merge(merged_df, df, on=['Isolate', 'Stx_type'], how='outer')

# Remove duplicate rows
merged_df = merged_df.drop_duplicates()

# Save the merged data to a CSV file
merged_df.to_csv("../../result/stx/merged_virulencefinder_blast_bakta_panaroo.csv", index=False)


