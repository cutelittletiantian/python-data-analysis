import matplotlib.pyplot as plt
import pandas as pd

# 配置项：防中文乱码
plt.rcParams["font.sans-serif"] = "SimHei"
# 坐标纸张大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]

# 读取2020.1.22到2020.7.27某地疫情感染情况
dfPandemic = pd.read_csv(filepath_or_buffer="virus.csv")

# x轴：时间（转datetime）
xDateTime = pd.to_datetime(dfPandemic["Date"])
# y轴：死亡率数据 = 确诊数 / 死亡数
yDeathRate = dfPandemic["Deaths"] / dfPandemic["Confirmed"]

# 绘制折线图
# 图例: 每日死亡率
# 折线颜色：橙色
# 点样式：实心圆
plt.plot(
    xDateTime, yDeathRate,
    label="每日死亡率",
    marker="o",
    color="orange"
)

# x轴和y轴名称：日期、死亡率
plt.xlabel(xlabel="日期")
plt.ylabel(ylabel="死亡率")
# 图表标题：2020年1月22日至2020年7月27日病毒死亡率走势
plt.title(label="2020年1月22日至2020年7月27日病毒死亡率走势")

# 显示图例
plt.legend()
# 展示图表
plt.show(block=False)
