import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# 配置坐标纸大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取订单销售情况数据（33w条数据，还是挺多的）
df = pd.read_csv(filepath_or_buffer="RFM.csv", usecols=["InvoiceDate", "Amount"])
# print(df.columns)
# Index(['Unnamed: 0', 'InvoiceNo', 'CustomerCode', 'InvoiceDate', 'Amount'], dtype='object')

# 按日期分组、计数、聚合
dfCountByDate = df.groupby(by="InvoiceDate").count()
dfSumByDate = df.groupby(by="InvoiceDate").sum()

# 绘图(2行1列)
fig, ax = plt.subplots(nrows=2, ncols=1)

# 子图1
# 日期与订单金额的柱状图：
# x轴数据为日期，
# y轴数据为每日销售额，
# 柱状图颜色为"orange"，
# x轴标题为"时间"，
# y轴标题为"当日销售总额(千万)"，
# x轴刻度旋转90度
curAxes = ax[0]  # type: Axes
curAxes.bar(x=dfSumByDate.index, height=dfSumByDate["Amount"], color="orange")
curAxes.set_xlabel(xlabel="时间")
curAxes.set_ylabel(ylabel="当日销售总额(千万)")
for x_tick in curAxes.get_xticklabels():
    x_tick.set_rotation(s=90)

# 子图2
# 日期与订单数量的柱状图：
# x轴数据为日期，
# y轴数据为当日的订单数，
# 柱状图颜色为"blue"，
# x轴标题为"时间"，
# y轴标题为"当日订单数"，
# x轴刻度旋转90度
curAxes = ax[1]  # type: Axes
curAxes.bar(x=dfCountByDate.index, height=dfCountByDate["Amount"], color="blue")
curAxes.set_xlabel(xlabel="时间")
curAxes.set_ylabel(ylabel="当日订单数")
for x_tick in curAxes.get_xticklabels():
    x_tick.set_rotation(s=90)

# 调整布局
plt.tight_layout()
# 显示图像
plt.show()
