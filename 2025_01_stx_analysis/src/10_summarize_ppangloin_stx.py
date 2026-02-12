import pandas as pd

# Read the TSV file
df = pd.read_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/ppanggolin_complete_result/result/stx_presence_absence.tsv', sep='\t')

stx_rows = df[df['Gene'].str.contains('stx', case=False)]
result_df = pd.DataFrame(columns=['Isolate', 'Stx_type', 'Count'])

for column in df.columns[1:]:
    sample_name = column.split('_')[0]
    gene_count = {}
    for index, row in stx_rows.iterrows():
        gene = row['Gene']
        if row[column] == 1:
            if gene in gene_count:
                gene_count[gene] += 1
            else:
                gene_count[gene] = 1
    for gene, count in gene_count.items():
        result_df = pd.concat([result_df, pd.DataFrame({'Isolate': [sample_name], 'Stx_type': [gene], 'Count': [count]})], ignore_index=True)

# Save the result to the output file
result_df.to_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/ppanggolin_result/stx_ppanggolin_complete.csv', index=False)
