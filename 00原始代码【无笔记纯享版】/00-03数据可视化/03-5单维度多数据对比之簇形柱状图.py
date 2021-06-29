import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

# 配置字体
plt.rcParams["font.sans-serif"] = "simhei"
# 图形放大
plt.rcParams["figure.figsize"] = (12.8, 10)

# 单维度多数据
df = pd.read_csv(filepath_or_buffer="resources/书店每月销量数据.csv")  # type: DataFrame
# print(df.columns)
# Index(['month', 'first_floor', 'second_floor', 'third_floor', 'sum'], dtype='object')

# x轴为月份，同一个x轴下展示出多个楼层y轴的数据（这一步要去找文档），图例自动会显示
df.plot(kind="bar", x="month", y=["first_floor", "second_floor", "third_floor"])

# 设置x轴和y轴名称分别为：月份和销量
plt.xlabel(xlabel="月份")
plt.ylabel(ylabel="销量")
# 标题：2019年8月至2020年7月书店每月各楼层销量走势
plt.title(label="2019年8月至2020年7月书店每月各楼层销量走势")

# 显示图像
plt.show()
