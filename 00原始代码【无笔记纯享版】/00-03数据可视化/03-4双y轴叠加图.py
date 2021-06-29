import pandas as pd
import matplotlib.pyplot as plt

# 配置字体
plt.rcParams["font.sans-serif"] = "simhei"
# 配置图宽
plt.rcParams["figure.figsize"] = (12.8, 4.8)

# 读取文件
df = pd.read_csv(filepath_or_buffer="resources/每月曝光量和转化率.csv")
# print(df.columns)
# 每月销量（"sum"）、广告曝光量（"exposure"）和 转化率（"CVR"）
# Index(['month', 'sum', 'exposure', 'CVR'], dtype='object')

# 月份-曝光柱状图
# 颜色：天蓝色
# 图例：PV
plt.bar(
    df["month"], df["exposure"],
    color="skyblue",
    label="PV"
)
# x轴和y轴名称：月份和曝光量
plt.xlabel(xlabel="月份")
plt.ylabel(ylabel="曝光量")
# 显示图例（为防止与折线图遮挡，这里调整一下位置，默认右上角，这个放左上角去）
plt.legend(loc="upper left")

# 当第一个图像绘制完成后，共享当前x轴，图表右侧添加一个新y轴
plt.twinx()

# 月份-转化率折线图
# 点的形状：圆形
plt.plot(
    df["month"], df["CVR"],
    marker="o",
    label="CVR"
)
# y轴名称：转化率
plt.ylabel(ylabel="转化率")
# 显示图例
plt.legend()

# 显示图像
plt.show()
