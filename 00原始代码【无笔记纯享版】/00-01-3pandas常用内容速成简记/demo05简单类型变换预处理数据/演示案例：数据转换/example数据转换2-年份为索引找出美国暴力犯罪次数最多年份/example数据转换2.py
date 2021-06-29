import pandas as pd
from pandas import DataFrame

# 美国50多年来的犯罪数据
df = pd.read_csv(filepath_or_buffer="US_Crime_Rates_1960_2014.csv")
# print(df.columns)

# 以年份为索引
df = df.set_index(keys="年份")
# print(df)

# 例如：查找暴力犯罪最频繁的年份
violentMax = df["暴力犯罪"].idxmax()
print(f"暴力犯罪发生最多的年份是{violentMax}")
