import pandas as pd
from pandas import DataFrame

df = pd.read_csv(filepath_or_buffer="drinks.csv")  # type: DataFrame

# 缺项默认补0
df.fillna(value=0, inplace=True)

# df.info()
print(f"啤酒总消耗量是{df['啤酒消耗'].sum()}")
