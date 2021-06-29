import pandas

# 读取用户RFM统计后的得分表
df = pandas.read_csv(filepath_or_buffer="ecom_data_rfm.csv")
# print(df.columns)
# Index(['CustomerID', 'rankR', 'rankF', 'rankM'], dtype='object')


# 高价值用户(R/M/F均大于3)
seHighValue = df[(df["rankR"] > 3) & (df["rankF"] > 3) & (df["rankM"] > 3)]["CustomerID"]

# 重点发展用户(R/M大于3，F小于等于3)
seDevelop = df[(df["rankR"] > 3) & (df["rankF"] <= 3) & (df["rankM"] > 3)]["CustomerID"]

# 重点潜力用户(R/F小于等于3，M大于3)
sePotential = df[(df["rankR"] <= 3) & (df["rankF"] <= 3) & (df["rankM"] > 3)]["CustomerID"]

# 以及重点唤回用户(M/F大于3，R小于等于3)
seCallback = df[(df["rankR"] <= 3) & (df["rankF"] > 3) & (df["rankM"] > 3)]["CustomerID"]

print(f"高价值用户:{seHighValue.values}")
print(f"重点发展用户:{seDevelop.values}")
print(f"重点潜力用户:{sePotential.values}")
print(f"重点唤回用户:{seCallback.values}")
