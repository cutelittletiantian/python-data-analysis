import pandas as pd
import matplotlib.pyplot as plt

# 配置绘图的坐标纸大小和中文字体
plt.rcParams["figure.figsize"] = [12.8, 9.6]
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取1年来快递站点的数据
df = pd.read_csv(filepath_or_buffer="近一年快递信息.csv")
# print(df.columns)
# Index(['日期', '揽收量', '发出量', '今日支出'], dtype='object')

# 预处理：日期转为时间类型并设置主键
df["日期"] = pd.to_datetime(arg=df["日期"])
df.set_index(keys="日期", inplace=True)

# 巨大波动平滑处理：揽收量和发出量的每7日的移动平均值
# 揽收量
seMovAvg7dCollect = df["揽收量"].rolling(window=7, min_periods=1).mean()
# 发出量
seMovAvg7dCoSend = df["发出量"].rolling(window=7, min_periods=1).mean()

# 绘制原始数据和揽收量7日移动均线图
plt.subplot(2, 1, 1)
plt.plot(seMovAvg7dCollect.index, seMovAvg7dCollect.values, color="red", label="揽收量")
plt.plot(df.index, df["揽收量"], color="gray", label="揽收量（平滑前）")
plt.xlabel("日期")
plt.ylabel("揽收量")
# 图例显示
plt.legend()

# 绘制原始数据和发出量7日移动均线图
plt.subplot(2, 1, 2)
plt.plot(seMovAvg7dCoSend.index, seMovAvg7dCoSend.values, color="orange", label="发出量")
plt.plot(df.index, df["发出量"], color="skyblue", label="发出量（平滑前）")
plt.xlabel("日期")
plt.ylabel("发出量")
# 图例显示
plt.legend()

# 显示图像
plt.show()
