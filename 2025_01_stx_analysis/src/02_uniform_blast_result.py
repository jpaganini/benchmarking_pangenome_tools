import csv

# open old file and new file
with open('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/stx_assembly_contig_number.csv', 'r', newline='') as input_file, open('/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/uniformed_stx_assembly_contig_number.csv', 'w', newline='') as output_file:
   
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    

    for row in csv_reader:
        # uniform stx gene name
        second_column_parts = row[1].split('_')
        

        new_value = '_'.join(second_column_parts[:2])
        

        row.append(new_value)
        

        csv_writer.writerow(row)
