import pandas as pd
from sas7bdat import SAS7BDAT

# 定义输入的 .sas7bdat 文件路径和输出的 .csv 文件路径
input_file = 'qpm0rlb61x6ixroi7.sas7bdat'
output_file = 'qpm0rlb61x6ixroi7.csv'

# 使用 SAS7BDAT 读取 .sas7bdat 文件
with SAS7BDAT(input_file) as reader:
    df = reader.to_data_frame()

# 将 DataFrame 保存为 .csv 文件，防止乱码，使用utf8保存
df.to_csv(output_file, index=False, encoding='utf-8')

# df.to_csv(output_file, index=False)

print(f'文件已成功转换并保存为 {output_file}')