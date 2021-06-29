import matplotlib.pyplot as plt
import pandas as pd

# 配置消除中文乱码
plt.rcParams["font.sans-serif"] = "SimSun"
# 调整整体宽度，避免x轴全部叠在了一起
plt.rcParams["figure.figsize"] = (12.8, 4.8)

print(plt.rcParams)

# 读取月销量数据
df = pd.read_csv(filepath_or_buffer="resources/书店每月销量数据.csv")

# 核心必选参数：x轴（月份）和y轴（总销量）取值
# 线颜色：橙色
# 点形状为圆
# 图例：每月总销量
plt.plot(
    df["month"],
    df["sum"],
    color="orange",
    marker="o",
    label="每月总销量"
)

# x轴、y轴名字分别为“月份”“销量”
plt.xlabel(xlabel="月份")
plt.ylabel(ylabel="销量")
# 标题为“2019年8月至2020年7月书店每月销量走势”
plt.title(label="2019年8月至2020年7月书店每月销量走势")

# 显示图例
plt.legend()
# 显示图像
plt.show()
