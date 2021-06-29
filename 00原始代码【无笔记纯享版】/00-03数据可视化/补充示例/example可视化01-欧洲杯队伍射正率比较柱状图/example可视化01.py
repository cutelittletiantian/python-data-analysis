import pandas as pd
import matplotlib.pyplot as plt

# 读取2012年欧洲杯部分数据

df = pd.read_csv(filepath_or_buffer="Euro2012.csv")
print(df.columns)
print(plt.rcParams)

# 配置中文乱码解决方案
plt.rcParams["font.sans-serif"] = "simhei"

# x轴数据
xTeam = df["Team"]
# y轴数据：射正率（转数值）
yShootingAccuracy = df["Shooting Accuracy"].str.strip("%").astype(float) / 100
# y轴数据：传正率（转数值）
# yPassingAccuracy = df["Passing Accuracy"].str.strip("%").astype(float) / 100

# 柱状图绘制
plt.bar(
    xTeam, yShootingAccuracy,   # 第一组数据（队名-射正率）
    label="射正率"
)
# plt.plot(
#     xTeam, yPassingAccuracy,
#     label="传正率", scaley=False
# )

# x轴标签和y轴标签分别设置：
plt.xlabel(xlabel="队名")
plt.ylabel(ylabel="射正率")
# 图表标题设置
plt.title(label="2012年欧洲杯各球队射正率柱状图")

# 显示图例
plt.legend()
# 显示图片
plt.show()
