import pandas as pd

# 读取主流酒类的世界消费数据表
df = pd.read_csv(filepath_or_buffer="drinks.csv")
# print(df.columns)
# Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings',
#        'total_litres_of_pure_alcohol', 'continent'],
#        dtype='object')

# 取出啤酒、白酒、红酒、洲这几个列
dfDrinks = df[["beer_servings", "spirit_servings", "wine_servings", "continent"]]

# 按洲分组，计算各种酒类消耗均值和中位数
# 均值
print(dfDrinks.groupby(by="continent").mean())
# 中位数
print(dfDrinks.groupby(by="continent").median())

# 按洲分组，计算各种酒类消耗最值。这里就只输出个白酒的最值算鸟...
# 最大
print(dfDrinks.groupby(by="continent")["spirit_servings"].max())
# 最小
print(dfDrinks.groupby(by="continent")["spirit_servings"].min())
