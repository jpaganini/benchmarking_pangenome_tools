import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    processed_rows = []
    for row in rows:
        if len(row) >= 9:
            # 提取第一列、第三列和第九列的内容
            first_column = row[0]
            third_column = row[2].split('-')[0]  # 只保留第三列元素被"-"分割后的第一部分内容
            ninth_column = row[8]
            # 修改第三列元素，将其改写为两个元素，分别占两行
            third_column_A = f"{third_column}_A"
            third_column_B = f"{third_column}_B"
            # 构造处理后的行
            processed_row_A = [first_column, third_column_A, ninth_column]
            processed_row_B = [first_column, third_column_B, ninth_column]
            processed_rows.extend([processed_row_A, processed_row_B])

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(processed_rows)

# 调用示例
input_file = '/hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_complete/stx_complete_results_deduplicate.csv'
output_file = '/hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_complete/stx_complete_separate_subunits.csv'
process_csv(input_file, output_file)
