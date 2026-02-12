import os
import csv

def count_elements_in_files(folder_path, output_file):
     # write column name
    with open(output_file, 'w') as output:
        writer = csv.writer(output, delimiter=',')
        writer.writerow(['Isolate', 'Stx_gene', 'No._of_contig'])
    # save contig number
    element_counts = {}
 
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv') and '+' in filename:
            file_path = os.path.join(folder_path, filename)
            element_counts = {}
            with open(file_path, 'r') as file:
                reader = csv.reader(file, delimiter='\t')
                for row in reader:
                    # make sure have enough number
                    if len(row) > 1:
                        # element of second column
                        element = row[1]
                       
                        element_counts[element] = element_counts.get(element, 0) + 1
                        print(element_counts)

        # write output
        with open(output_file, 'a') as output:
            writer = csv.writer(output, delimiter=',')
            for element, count in element_counts.items():
                print(element)
                # get file name
                source_file = filename.split('+')[0]
                print(source_file)
                writer.writerow([source_file, element, count])


folder_path = '/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_1_blast_stx/result/' 
output_file = '/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/stx_assembly_contig_number.csv'  
count_elements_in_files(folder_path, output_file)
