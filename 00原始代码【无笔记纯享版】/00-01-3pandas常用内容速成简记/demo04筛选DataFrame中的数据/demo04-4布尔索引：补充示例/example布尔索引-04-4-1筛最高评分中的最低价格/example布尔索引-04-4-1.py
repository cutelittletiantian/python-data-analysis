import pandas as pd
from pandas import DataFrame

resourceFile = "bestsellers.csv"

# 取出表数据
data = pd.read_csv(filepath_or_buffer=resourceFile)

# Index(['书名', '作者', '评分', '被查看次数', '价格', '年份', '体裁'], dtype='object')
# print(data.columns)

# 最高评分“中”的最低价格(基于最高评分接着细粒度筛，千万注意这里不是重新筛)

# 筛选数据结果result从原始data开始。深拷贝，不是浅拷贝。
result = data
# 筛出最高评分
result = result[result["评分"] == result["评分"].max()]
# 在最高评分的基础上，筛出最低价格
result = result[result["价格"] == result["价格"].min()]

# 下面这样做是不对的，看似可以实际报错
# result = result[result["评分"] == result["评分"].max()][result["价格"] == result["价格"].min()]

# 输出结果
print(result)
