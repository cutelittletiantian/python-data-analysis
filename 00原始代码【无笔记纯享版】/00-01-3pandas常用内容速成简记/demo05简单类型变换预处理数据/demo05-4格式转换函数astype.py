import pandas as pd

# 定义一个字典
data = {"rank": [1, 2, 3, 4], "GDP": [80855, 77388, 68024, 47251]}

# 构造一个DataFrame
df = pd.DataFrame(data)
print(df)

# 定义一个01序列组成的列表
search = [0, 1, 0, 1]
# 构造成一个Series
se = pd.Series(search)
# 将se中的01，转换为False/True的布尔索引序列，并重新存储给se
se = se.astype(bool)
# 输出此时se，可以看到是一个布尔序列
print(se)

# 用布尔索引筛选，输出筛选结果
print(df[se])
