import pandas as pd
from datetime import datetime, timedelta

# 读取文件
df = pd.read_csv(filepath_or_buffer="兴兴药店2018年销售数据.csv")
# ['购药时间', '社保卡号', '商品编码', '商品名称', '销售数量', '应收金额', '实收金额']
# print(df.columns)

# 预处理：时间类型转化
df["购药时间"] = pd.to_datetime(arg=df["购药时间"])

# 计算出2018年一段时间以来药店患者的日均消费次数、日均消费金额和客单价
# 日均消费次数 = 总消费次数 / 天数
# 日均消费金额 = 总消费金额（实收金额） / 天数
# 客单价 = 总消费金额 / 总消费次数

# 总消费次数
totalPurchaseCount = len(df.index)

# 2018年记录在册的第一天
startTime = df.loc[0, "购药时间"]  # type: datetime
# print(startTime)
# 2018年记录在册的最后一天（不支持复数下标）
endTime = df.loc[totalPurchaseCount - 1, "购药时间"]  # type: datetime
# print(endTime)
# 记录在册天数
dayCount = (endTime - startTime).days

# 总消费金额
totalPayment = df["实收金额"].sum()

print(f"日均消费次数是{totalPurchaseCount / dayCount}，"
      f"日均收入金额为{totalPayment / dayCount}，"
      f"客单价为{totalPayment / totalPurchaseCount}")