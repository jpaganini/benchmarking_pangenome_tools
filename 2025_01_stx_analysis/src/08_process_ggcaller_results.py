import pandas as pd

# Read the CSV file
df = pd.read_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/ggcaller_complete_result/gene_presence_absence.csv")

# Handle NaN values, replacing them with empty strings
df.fillna('', inplace=True)

# Find rows where the Annotation column contains STX
df = df[df['Annotation'].str.contains('STX')]

# Create a dictionary to store gene counts for all samples
total_gene_counts = {}

# Iterate over each sample column
for sample_column in df.columns[3:]:
    sample_name = sample_column.split('_')[0]
    # Create a dictionary to store gene counts for the current sample
    gene_counts = {}
    
    # Iterate over each row
    for index, row in df.iterrows():
        annotation_parts = row['Annotation'].split('|')
        gene_parts = annotation_parts[2].split('_')
        gene = gene_parts[0]

        # If the current sample column value is not empty, increment the count
        if row[sample_column] != '':
            if gene not in gene_counts:
                gene_counts[gene] = 0
            gene_counts[gene] += 1
    
    # Add the current sample's gene counts to the total gene counts
    for gene, count in gene_counts.items():
        if sample_name not in total_gene_counts:
            total_gene_counts[sample_name] = {}
        if gene not in total_gene_counts[sample_name]:
            total_gene_counts[sample_name][gene] = 0
        total_gene_counts[sample_name][gene] += count

# Create the output file
output_data = []
for sample, genes in total_gene_counts.items():
    for gene, count in genes.items():
        gene = gene[0:3].replace('STX', 'stx') + '_' + gene[3:]
        output_data.append({'Isolate': sample, 'Stx_type': gene, 'count': count})

output_df = pd.DataFrame(output_data)

# Save the output file
output_df.to_csv("/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/ggcaller_result/ggcaller_complete_stx.csv", index=False)
