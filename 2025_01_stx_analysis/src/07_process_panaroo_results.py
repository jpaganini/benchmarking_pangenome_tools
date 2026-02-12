import pandas as pd

# Read the CSV file
df = pd.read_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/panaroo_complete_result/gene_data.csv')

# Rename the columns to 'Isolate' and 'complete_description'
df.rename(columns={'gff_file': 'Isolate', 'description': 'complete_description'}, inplace=True)

# Keep only the first part of each element in the 'Isolate' column, splitting by '_'
df['Isolate'] = df['Isolate'].str.split('_').str[0]

# Retain only rows where the 'complete_description' column contains the word 'Shiga'
df = df[df['complete_description'].str.contains('Shiga', case=False)]

# Add a new column 'Stx_type' by combining the 3rd and 5th words of 'complete_description' with an underscore
df['Stx_type'] = df['complete_description'].str.split().str[2] + '_' + df['complete_description'].str.split().str[4]

# Change the first letter of 'Stx_type' from 'S' to 's' if it starts with 'S'
df['Stx_type'] = df['Stx_type'].apply(lambda x: x if x[0] != 'S' else 's' + x[1:])

# Select the relevant columns
selected_columns = df[['Isolate', 'complete_description', 'Stx_type']]

# Count the number of occurrences of each row, adding the count as a new column
selected_columns['No_of_stx_gene_panaroo_complete'] = df.groupby(df.columns.tolist()).transform('size')

# Remove duplicate rows
selected_columns.drop_duplicates(inplace=True)

# Write the result to a new CSV file
selected_columns.to_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/panaroo_result/panaroo_complete_stx.csv', index=False)

# Print a confirmation message
print("Modified selected columns have been successfully written to csv")
