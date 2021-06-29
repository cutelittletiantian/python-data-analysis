import pandas as pd
import matplotlib.pyplot as plt

# 配置语言字体
plt.rcParams["font.sans-serif"] = "simhei"
# 配置坐标纸大小
plt.rcParams["figure.figsize"] = (6.4, 8.2)

# 打开文件
df = pd.read_csv(filepath_or_buffer="bank.csv")
# print(df.columns)
# Index(['年份', '通货膨胀率', '价格水平'], dtype='object')

# 年份与价格水平比较：柱状图
# 颜色设置为天蓝色，图例设置为"货币水平"
plt.bar(
    df["年份"], df["价格水平"],
    color="skyblue",
    label="货币水平"
)
# x轴标题为"年份"，y轴标题为"价格水平"
plt.xlabel(xlabel="年份")
plt.ylabel(ylabel="价格水平")
# 图例显示在左上角，防止与折线图遮挡
plt.legend(loc="upper left")

# 共享x轴
plt.twinx()

# 另添加一个y轴，画折线图
# 展示年份与通货膨胀率，并将折线的标记样式设置为圆形，图例设置为"通货膨胀率"
plt.plot(
    df["年份"], df["通货膨胀率"],
    marker="o",
    label="通货膨胀率"
)
# y轴标题设置为"通货膨胀率"
plt.ylabel(ylabel="通货膨胀率")
# 显示图例，默认右上角位置
plt.legend()

# 显示叠加图表
plt.show()
