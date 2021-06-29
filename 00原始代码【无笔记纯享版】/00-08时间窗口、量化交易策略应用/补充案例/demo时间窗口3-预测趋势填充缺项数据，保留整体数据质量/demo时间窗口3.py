import pandas as pd
from pandas import Series

# 读取订单信息文件
df = pd.read_csv(filepath_or_buffer="最近一年单量信息.csv")
# print(df.columns)
# Index(['日期', '堂食单量', '外卖单量', '打包单量'], dtype='object')

# 找出有缺项数据的行数据
dfHasNull = df[df["堂食单量"].isnull() | df["外卖单量"].isnull() | df["打包单量"].isnull()]

# 计算原数据含缺项列的7日移动均值
se7dMovAvgTakeout = df["外卖单量"].rolling(window=7, min_periods=1).mean()  # type: Series

# 订单信息填入缺项为移动均值，保留整数
df.loc[dfHasNull.index, "外卖单量"] = se7dMovAvgTakeout[dfHasNull.index].round()

# 计算总单量
df["总单量"] = df["堂食单量"] + df["外卖单量"] + df["打包单量"]
print(df["总单量"])
