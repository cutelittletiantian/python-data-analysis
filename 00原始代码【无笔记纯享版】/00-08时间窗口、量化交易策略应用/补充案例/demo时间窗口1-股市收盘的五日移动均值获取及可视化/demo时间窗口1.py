import pandas as pd
import matplotlib.pyplot as plt

# 配置绘图的坐标纸大小和中文字体
plt.rcParams["figure.figsize"] = [12.8, 9.6]
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取2个股市数据文件
dfGongshang = pd.read_csv(filepath_or_buffer="gongshang.csv")
dfMinsheng = pd.read_csv(filepath_or_buffer="minsheng.csv")
# print(dfGongshang.columns)
# print(dfMinsheng.columns)
# Index(['date', 'code', 'open', 'high', 'low', 'close', 'preclose', 'volume',
#        'amount', 'adjustflag', 'turn', 'tradestatus', 'pctChg', 'isST'],
#       dtype='object')

# 预处理：date列转为时间类型
dfGongshang["date"] = pd.to_datetime(arg=dfGongshang["date"])
dfMinsheng["date"] = pd.to_datetime(arg=dfMinsheng["date"])
# 时间类型转index
dfGongshang.set_index(keys="date", inplace=True)
dfMinsheng.set_index(keys="date", inplace=True)

# 5日移动均值的计算，以close收盘价为基准
dfMovAvg5dGS = dfGongshang.rolling(window=5, min_periods=1).mean()
dfMovAvg5dMS = dfMinsheng.rolling(window=5, min_periods=1).mean()

# 数据可视化
# 绘制B、C三支股票的5日移动均线图
plt.plot(dfMovAvg5dGS.index, dfMovAvg5dGS["close"], color="blue")
plt.plot(dfMovAvg5dMS.index, dfMovAvg5dMS["close"], color="orange")
plt.xlabel("日期")
plt.ylabel("收盘价")
plt.show()
