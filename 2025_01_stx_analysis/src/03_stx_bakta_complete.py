import os
import csv

# Path to the main folder
base_folder = '/hpc/uu_vet_iras/pliu/remove_bad_result/bakta_complete_result/'

# Path to the output file
output_file = '/hpc/uu_vet_iras/pliu/remove_bad_result/2024_5_5_merge_blast_virulencefinder_annotaion/result/stx_bakta_annotation_complete.csv'

# Iterate over each subfolder in the main folder
with open(output_file, 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Isolate", "bakta_annotation_complete"])
    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)
        print(folder)
        # Check if it is a folder
        if os.path.isdir(folder_path):
            gff3_file = os.path.join(folder_path, folder + '_complete_genome.gff3')
            
            # Check if the .gff3 file exists
            if os.path.isfile(gff3_file):
                with open(gff3_file, 'r') as f:
                    # Read each line of the file
                    for line in f:
                        # Check if it contains ";" and includes both "Name" and "Stx"
                        if ";" in line and "Name=" in line and "Stx" in line:
                            # Split the line by ";"
                            elements = line.strip().split(";")
                            for element in elements:
                                # Find the element containing both "Name" and "Stx"
                                if "Name=" in element and "Stx" in element:
                                    # Record the part after "Name="
                                    name = element.split("Name=")[1]
                                    out_file.write(folder + ',' + name + '\n')
