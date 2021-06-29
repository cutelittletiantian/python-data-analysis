import pandas as pd

# 读取赛事和进球数据
dfSoccer = pd.read_csv(filepath_or_buffer="score.csv")
# print(dfSoccer.columns)
# Index(['日期', '球队', '进球', '赛事'], dtype='object')

# 预处理：日期类型为datetime
dfSoccer["日期"] = pd.to_datetime(arg=dfSoccer["日期"])

# 赛事分组、月份重采样、总进球数聚合
dfByEvent = dfSoccer.groupby(by="赛事").resample(rule="M", on="日期").sum()

print(dfByEvent)
