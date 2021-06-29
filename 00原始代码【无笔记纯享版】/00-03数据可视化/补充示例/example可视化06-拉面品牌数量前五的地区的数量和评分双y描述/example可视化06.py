import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.text import Text
from pandas import DataFrame

# 配置图表尺寸
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = "SimHei"

# 读取拉面数据的文件
dfRamen = pd.read_csv(filepath_or_buffer="ramenRatings.csv")  # type: DataFrame
# print(dfRamen.columns)
# Index(['Area', 'Bowl', 'Cup', 'Pack', 'rating'], dtype='object')

# 预处理：df添加一个列sum，存储各品牌拉面数量总和
dfRamen["sum"] = dfRamen[["Bowl", "Cup", "Pack"]].sum(axis=1)
# 排序：order by "sum"，降序
dfRamen = dfRamen.sort_values(by="sum", ascending=False)
# 选出前5，limit 5
dfRamenFirst5 = dfRamen[:5]

# 绘制前五的碗装、杯装、袋装拉面品牌的簇形柱状图，分别设置x轴和y轴的标题为"国家/地区"和"品牌总量"
ax1 = dfRamenFirst5.plot(
    kind="bar", x="Area", y=["Bowl", "Cup", "Pack"],
    xlabel="国家/地区", ylabel="品牌总量",
    label=["碗装", "杯装", "袋装"]
)  # type: Axes

# 增加双y轴
# plt.twinx()

# # 绘制评分的折线图，点样式为星星状，颜色为深红色（crimson）
# plt.plot(dfRamenFirst5["Area"], dfRamenFirst5["rating"],
#          marker="*", color="crimson")
# # y轴标题为评分
# plt.ylabel(ylabel="评分")

ax2 = ax1.twinx()

ax2 = dfRamenFirst5.plot(
    kind="line", x="Area", y=["rating"],
    xlabel="国家/地区", ylabel="评分",
    secondary_y=["rating"], ax=ax2,
    marker="*", color="crimson",
    label=["评分"]
)  # type: Axes

ax2.legend(loc="upper left")

# 图例已自动显示，显示图像
plt.show()
