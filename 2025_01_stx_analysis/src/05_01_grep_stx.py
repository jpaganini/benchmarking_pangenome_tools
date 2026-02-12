import os
import pandas as pd

# 定义文件夹路径
folder_path = "/hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_complete/"

# 获取文件夹中所有子文件夹的名字
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

# 创建一个空的DataFrame来保存结果
result_df = pd.DataFrame(columns=['Folder', 'Database', 'Virulence factor', 'Identity', 'Query / Template length', 'Contig', 'Position in contig', 'Protein function', 'Accession number'])

# 遍历每个子文件夹
for subfolder in subfolders:
    # 构建results_tab.tsv文件路径
    tsv_path = os.path.join(subfolder, 'results_tab.tsv')
    
    # 检查文件是否存在
    if os.path.exists(tsv_path):
        # 读取tsv文件为DataFrame
        df = pd.read_csv(tsv_path, sep='\t')
        
        # 找到含有'Virulence factor'列中含有'stx'的行
        stx_rows = df[df['Virulence factor'].str.contains('stx', case=False, na=False)]
        
        # 添加到结果DataFrame中
        if not stx_rows.empty:
            stx_rows['Folder'] = os.path.basename(subfolder)
            result_df = pd.concat([result_df, stx_rows], ignore_index=True)

# 将结果保存为csv文件
result_df.to_csv('/hpc/uu_vet_iras/pliu/remove_bad_result/virulencefinder_complete/stx_results.csv', index=False)
