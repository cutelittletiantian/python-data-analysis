import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series

# 读取纽约房租表
df = pd.read_csv(filepath_or_buffer="newyork.csv", encoding="utf-8")
# print(df.columns)
# Index(['name', 'neighborhood', 'price'], dtype='object')

# 清洗数据：填充缺项为默认值unknown，这个缺项不影响后续的分析
df["name"].fillna(value="unknown", inplace=True)

# 按照街区neighborhood分组求各街区房租的均值
serisByNeighborhood = df.groupby(by="neighborhood").mean()["price"]  # type: Series

# 可视化街区-房租柱状图
# 配置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]

# 柱体颜色设置为green，图例设置为"均值"，x轴标题设置为"街区"，y轴标题设置为"房价均值"
plt.bar(
    x=serisByNeighborhood.index, height=serisByNeighborhood.values,
    color="green", label="均值"
)
plt.xlabel(xlabel="街区")
plt.ylabel(ylabel="房价均值")
# 显示图例
plt.legend()
# 显示图像
plt.show()
