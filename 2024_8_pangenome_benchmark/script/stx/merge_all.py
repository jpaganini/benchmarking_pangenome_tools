import pandas as pd

# Read all CSV files
df1 = pd.read_csv("../../result/merged_virulencefinder_blast_bakta_panaroo_remove_type.csv")
df12 = pd.read_csv("../../result/ggcaller_result/ggcaller_assembly_stx.csv")
df13 = pd.read_csv("../../result/ggcaller_result/ggcaller_1%_complete_stx.csv")
df14 = pd.read_csv("/../../result/ggcaller_result/ggcaller_10%_complete_stx.csv")
df15 = pd.read_csv("../../result/ggcaller_result/ggcaller_50%_complete_stx.csv")
df16 = pd.read_csv("../../result/ggcaller_result/ggcaller_90%_complete_stx.csv")
df17 = pd.read_csv("../../result/ggcaller_result/ggcaller_99%_complete_stx.csv")
df18 = pd.read_csv("../../result/ggcaller_result/ggcaller_complete_stx.csv")
df19 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_assembly.csv")
df20 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_1%_complete.csv")
df21 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_10%_complete.csv")
df22 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_50%_complete.csv")
df23 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_90%_complete.csv")
df24 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_99%_complete.csv")
df25 = pd.read_csv("../../result/ppanggolin_result/stx_ppanggolin_complete.csv")

merged_df = df1

for df in [df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24, df25]:
    merged_df = pd.merge(merged_df, df, on=['Isolate', 'Stx_type'], how='outer')
    
merged_df = merged_df.drop_duplicates()

merged_df = merged_df.fillna(0)

# Save the merged data as a CSV file
merged_df.to_csv("../../result/merged_all_stx_infor.csv", index=False)

