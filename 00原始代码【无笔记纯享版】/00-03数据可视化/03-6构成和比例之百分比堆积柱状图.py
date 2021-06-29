import pandas as pd
import matplotlib.pyplot as plt

# 配置字体
plt.rcParams["font.sans-serif"] = "simhei"
# 配置坐标纸大小
plt.rcParams["figure.figsize"] = (12.8, 10)

# 读取文件
df = pd.read_csv(filepath_or_buffer="resources/书店每月销量数据百分比.csv")
# print(df.columns)
# Index(['month', '一楼', '二楼', '三楼'], dtype='object')

# 【这一步要查文档】绘制堆叠柱状图stacked bar，图例自动显示
df.plot(kind="bar", stacked=True, x="month", y=["一楼", "二楼", "三楼"])

# x轴标题设置为"月份"
plt.xlabel("月份")
# y轴标题设置为"占比"
plt.ylabel("占比")
# 图表标题设置为"2019年8月至2020年7月书店每月销量占比"
plt.title("2019年8月至2020年7月书店每月销量占比")

# 显示
plt.show()
