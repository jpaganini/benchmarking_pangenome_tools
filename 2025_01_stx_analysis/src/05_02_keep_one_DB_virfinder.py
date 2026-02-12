import pandas as pd

# read csv files
df = pd.read_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_complete/stx_complete_results.csv')

# save virulence_ecoli lines
df = df[df['Database'] != 'stx']

# save modified_file
df.to_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_complete/stx_complete_results_deduplicate.csv', index=False)
