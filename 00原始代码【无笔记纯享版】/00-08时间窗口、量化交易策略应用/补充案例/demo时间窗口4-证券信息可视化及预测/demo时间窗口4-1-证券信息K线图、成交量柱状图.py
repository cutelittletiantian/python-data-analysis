import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
# import mpl_finance as mpf
from mplfinance import original_flavor as mpf
# from matplotlib.pylab import date2num
from matplotlib import style

# 配置绘图的坐标纸大小和中文字体
plt.rcParams["figure.figsize"] = [12.8, 9.6]
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取股市信息文件
dfStock = pd.read_csv(filepath_or_buffer="stock_data.csv", usecols=["date", "open", "close", "high", "low", "volume"])
# print(dfStock.columns)
# Index(['date', 'open', 'high', 'low', 'close', 'volume'], dtype='object')

# 挑选出"date", "open", "close", "high", "low", "volume"这6列，前5列顺序必须一致，所以这句话还有调整顺序的功效
dfStock = dfStock[["date", "open", "close", "high", "low", "volume"]]

# 预处理
# date列转化为时间格式
dfStock["date"] = pd.to_datetime(arg=dfStock["date"])
# 将日期转化为数字（数字为距离1970-01-01多少天）
# dfStock["date"] = dfStock["date"].apply(func=lambda x: date2num(x))
dfStock["date"] = dfStock["date"].apply(func=lambda x: (x - pd.to_datetime(arg="1970-1-1")).days)

# 先取前60个数据，转化为列表，方便画图使用，赋值给变量data_mat
dfMat = dfStock.loc[0: 60].values

# 数据可视化
# 设置背景颜色为黑色
plt.style.use(style="dark_background")
# 两个子图共享x轴，(1200/72, 480/72)为设置画布尺寸
fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(1200 / 72, 480 / 72))
# 绘制K线图
mpf.candlestick_ochl(ax=ax1, quotes=dfMat, colordown="green", colorup="red", width=0.3, alpha=1)
# x轴坐标转换为时间格式
ax1.xaxis_date()

# 绘制成交量volume柱状图
plt.bar(x=dfMat[:, "date"], height=dfMat[:, "volume"], width=0.5, label="volume")
# 设置标题为"K线和成交量图"
plt.title("K线和成交量图")
# 展示图例
plt.legend()

# 展示图片
plt.show()
