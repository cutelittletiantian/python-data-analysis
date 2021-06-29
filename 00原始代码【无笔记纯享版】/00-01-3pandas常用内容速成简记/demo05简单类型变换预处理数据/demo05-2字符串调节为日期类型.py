import pandas as pd

# 读取文件，赋值给变量df
df = pd.read_csv(filepath_or_buffer="resources/电商数据清洗.csv", usecols=["create_time", "pay_time"])
print(df)

# 将create_time和pay_time两列中字符串呈现的时间格式转化成datetime格式
df["create_time"] = pd.to_datetime(df["create_time"])
df["pay_time"] = pd.to_datetime(df["pay_time"])

# 输出此时的df
print(df)
