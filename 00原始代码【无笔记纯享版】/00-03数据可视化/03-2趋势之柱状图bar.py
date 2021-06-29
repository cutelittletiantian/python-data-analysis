import matplotlib.pyplot as plt
import pandas as pd

# 配置消除中文乱码
plt.rcParams["font.sans-serif"] = "SimSun"

# 读取月销量数据
df = pd.read_csv(filepath_or_buffer="resources/书店每月销量数据.csv")

# 核心必选参数：x轴（月份）和y轴（总销量）取值
# 柱子颜色：红色
# 柱子宽度：0.5
# 图例：每月总销量
plt.bar(
    df["month"],
    df["sum"],
    color="red",
    width=0.5,
    label="每月总销量"
)

# x轴、y轴标题设置为“标题”“销量”
plt.xlabel(xlabel="月份")
plt.ylabel(ylabel="销量")
# 标题设置：2019年8月至2020年7月书店每月销量走势
plt.title(label="2019年8月至2020年7月书店每月销量走势")

# 显示图例
plt.legend()
# 显示柱状图
plt.show()
