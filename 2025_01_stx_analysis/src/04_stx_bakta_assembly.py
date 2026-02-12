import os
import csv

# 大文件夹路径
base_folder = '/hpc/uu_vet_iras/pliu/remove_bad_result/bakta_assembly_result/'

# 输出文件路径
output_file = '/hpc/uu_vet_iras/pliu/remove_bad_result/stx_annotaion/stx_gene_annotation_assembly.csv'

# 遍历大文件夹中的每个小文件夹
with open(output_file, 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Sample", "Stx"])
    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)
        print(folder)
        # 检查是否是文件夹
        if os.path.isdir(folder_path):
            gff3_file = os.path.join(folder_path, folder + '_assembly.gff3')
            
            # 检查.gff3文件是否存在
            if os.path.isfile(gff3_file):
                with open(gff3_file, 'r') as f:
                    # 读取文件的每一行
                    for line in f:
                        # 检查是否含有";"并且包含Name和Stx
                        if ";" in line and "Name=" in line and "Stx" in line:
                            # 根据";"分割行
                            elements = line.strip().split(";")
                            for element in elements:
                                # 找到含有Name和Stx的元素
                                if "Name=" in element and "Stx" in element:
                                    # 记录除了"Name="之外的部分
                                    name = element.split("Name=")[1]
                                    out_file.write(folder + ',' + name + '\n')
