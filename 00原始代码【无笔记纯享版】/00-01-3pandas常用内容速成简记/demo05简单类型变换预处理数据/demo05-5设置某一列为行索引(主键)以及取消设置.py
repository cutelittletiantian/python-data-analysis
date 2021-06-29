import pandas as pd

data = {"provin": ["GD", "JS", "SD", "ZJ"], "rank": [1, 2, 3, 4], "GDP": [80855, 77388, 68024, 47251]}

# 构造一个df
df = pd.DataFrame(data)

# 使用set_index()函数，将provin这一列转化成index，赋值给new_df
new_df = df.set_index("provin")
# 输出new_df
print(new_df)
print()

# 使用reset_index()函数，将index转化成普通列，赋值给df
df = new_df.reset_index()
# 输出df
print(df)
