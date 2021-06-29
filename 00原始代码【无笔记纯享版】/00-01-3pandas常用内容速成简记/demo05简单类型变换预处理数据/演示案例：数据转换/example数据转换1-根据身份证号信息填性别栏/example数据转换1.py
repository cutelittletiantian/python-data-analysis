import pandas as pd

# 取出文件
df = pd.read_csv(filepath_or_buffer="住户信息.csv")
# print(df.columns)

# 身份证号列转为字符串
df["身份证号"] = df["身份证号"].astype(dtype=str)

# 取出身份证号的第13位判断性别：奇数男，偶数女
gender = [("男" if int(identity[12]) % 2 == 1 else "女") for identity in df["身份证号"]]
# print(gender)

# 补齐性别列的缺项
df["性别"] = gender
print(df)
