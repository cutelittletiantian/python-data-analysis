import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

# 配置坐标纸大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取美国各地牛油果价格数据
dfAvocado = pd.read_csv(filepath_or_buffer="avocado.csv")
# print(dfAvocado.columns)
# Index(['Date', 'AveragePrice', 'region'], dtype='object')

# 预处理：时间类型
dfAvocado["Date"] = pd.to_datetime(arg=dfAvocado["Date"])

# 按地区分组，按月份为频率进行重采样，聚合平均值
dfMonthlyByRegion = dfAvocado.groupby(by="region").resample(on="Date", rule="M").mean()  # type: DataFrame
# 选中纽约数据
dfMonthlyNewYork = dfMonthlyByRegion.loc["NewYork"]  # type: DataFrame
# 选中芝加哥数据
dfMonthlyChicago = dfMonthlyByRegion.loc["Chicago"]  # type: DataFrame
# 全美国每月平均价格
dfMonthlyAmerica = dfAvocado.resample(on="Date", rule="M").mean()  # type: DataFrame

# 绘制折线图
# 纽约数据，圆点，天蓝色，图例为“纽约价格水平”
plt.plot(dfMonthlyNewYork.index, dfMonthlyNewYork["AveragePrice"],
         marker="o", color="skyblue", label="纽约价格水平")
# 芝加哥数据，圆点，蓝色，图例为“芝加哥价格水平”
plt.plot(dfMonthlyChicago.index, dfMonthlyChicago["AveragePrice"],
         marker="o", color="blue", label="芝加哥价格水平")
# 全美国数据，圆点，绿色，图例为“全美价格水平”
plt.plot(dfMonthlyAmerica.index, dfMonthlyAmerica["AveragePrice"],
         marker="o", color="green", label="全美价格水平")
# x轴标题为"时间"，y轴标题设置为"价格水平"，图例显示在左上角
plt.xlabel(xlabel="时间")
plt.ylabel(ylabel="价格水平")
plt.legend(loc="upper left")

# 显示图像
plt.show()
