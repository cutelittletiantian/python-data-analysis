import pandas as pd
import matplotlib.pyplot as plt

# 配置中文字体
plt.rcParams["font.sans-serif"] = "simhei"

# 读取文件
df = pd.read_csv(filepath_or_buffer="video.csv")
# print(df.columns)
# Index(['播放量', '点赞量', '收藏/观看比例'], dtype='object')

# 绘制散点图
# 设置散点的大小来反映收藏/观看比例
plt.scatter(
    x=df["播放量"], y=df["点赞量"],
    s=df["收藏/观看比例"]
)

# x轴标题设置为观看次数，y轴标题设置为点赞量
plt.xlabel(xlabel="观看次数")
plt.ylabel(ylabel="点赞量")

# 显示图像
plt.show()
