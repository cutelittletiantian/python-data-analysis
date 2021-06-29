from datetime import datetime
import pandas as pd
from pandas import DataFrame
from pandas.core.resample import Resampler

# 读取西雅图好多年来的降水量数据

dfRainFall = pd.read_csv(filepath_or_buffer="seattleWeather.csv")
# print(dfRainFall.columns)
# Index(['日期', '降雨量'], dtype='object')

# 预处理：日期统一位时间类型
dfRainFall["日期"] = pd.to_datetime(arg=dfRainFall["日期"])

# 日期为索引，方便后续查找
# dfRainFall.set_index(keys="日期")

# 按年重采样、聚合
dfByYear = dfRainFall.resample(rule="Y", on="日期").sum()  # type: DataFrame

# 找出最大、最小年份
maxDateOfRain = dfByYear["降雨量"].idxmax()  # type: datetime
minDateOfRain = dfByYear["降雨量"].idxmin()  # type: datetime

print(f"历史降雨量最多的一年是{maxDateOfRain.year}年，最少的一年是{minDateOfRain.year}年")
