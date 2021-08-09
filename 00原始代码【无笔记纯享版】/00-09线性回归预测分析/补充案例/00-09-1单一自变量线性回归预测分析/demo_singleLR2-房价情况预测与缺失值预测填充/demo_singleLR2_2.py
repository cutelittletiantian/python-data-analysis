import pandas as pd
from pandas import DataFrame

# 利用上一问得到的线性回归模型，利用房价数据预测填充表格中缺失的房屋面积数据
# 该线性回归模型为：y=1.8367978324930496*x+2.0841163976083976，预测值x=(y-2.0841)/1.8368
# 系数
coefficient = 1.8368
# 截距
intercept = 2.0841

# 读取文件
df = pd.read_csv("成都市夜曲区房源数据.csv")
# print(df.columns)
# Index(['房屋总价/万', '建筑面积', '房屋用途', '房屋户型'], dtype='object')

# 预测房价
areaPredict = (df["房屋总价/万"] - intercept) / coefficient
df["建筑面积"].fillna(value=areaPredict[df[df["建筑面积"].isnull()].index], inplace=True)

# 预测房屋单价
df["房价单价（万元/平方）"] = df["房屋总价/万"] / df["建筑面积"]
# 输出查看填充结果
print(df["房价单价（万元/平方）"])
# 查看缺失是否被填充
df.info()
