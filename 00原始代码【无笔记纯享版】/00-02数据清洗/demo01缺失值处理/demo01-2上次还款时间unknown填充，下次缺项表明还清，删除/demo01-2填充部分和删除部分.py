import pandas as pd
from pandas import DataFrame

df = pd.read_csv(filepath_or_buffer="抽取样例信息表.csv")

# 查缺项数据
# df.info()

# 上次还款三列缺项默认置为unknown
df["上次还款日期"].fillna(value="unknown", inplace=True)
df["上次还款本金"].fillna(value="unknown", inplace=True)
df["上次还款利息"].fillna(value="unknown", inplace=True)
# 检查缺项是否还存在
# df.info()

# 已还清直接删除
df.drop(index=df[df["下次计划还款日期"].isnull()].index, inplace=True)
df.drop(index=df[df["下次计划还款本金"].isnull()].index, inplace=True)
df.drop(index=df[df["下次计划还款利息"].isnull()].index, inplace=True)
# 检查缺项是否还存在
df.info()
