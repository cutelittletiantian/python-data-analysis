import pandas as pd

# 读取文件
df = pd.read_csv("resources/电商数据清洗.csv", usecols=["pay_time"])

# 使用to_datetime函数，将pay_time这一列转化为时间类型，重新赋值给pay_time这一列
df["pay_time"] = pd.to_datetime(df["pay_time"])
# 将pay_time这一列转化为"%Y年%m月%d日"的格式，赋值给"日期"这一列
df["日期"] = df["pay_time"].dt.strftime("%Y年%m月%d日")
# 将pay_time这一列转化为"星期%u"的格式，赋值给"星期"这一列
df["星期"] = df["pay_time"].dt.strftime("星期%u")

# 输出这个df
print(df)
