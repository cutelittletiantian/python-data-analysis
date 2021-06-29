import pandas as pd
from pandas import Series

# 读取股票交易信息文件，取出日期、收盘价
dfStock = pd.read_csv(filepath_or_buffer="stock_data.csv", usecols=["date", "close"])
# print(dfStock.columns)
# Index(['date', 'close'], dtype='object')

# 预处理：date为时间类型，设置主键
dfStock["date"] = pd.to_datetime(arg=dfStock["date"])
dfStock.set_index(keys="date", inplace=True)

# 十日移动均值
dfMov10dMean = dfStock.rolling(min_periods=1, window=10).mean()

# 十日均线小于当日收盘的序列模型
se10dModel = dfMov10dMean["close"] < dfStock["close"]  # type: Series

# 相邻节点滚动，找买入拐点策略：均线由大于当日收盘变成小于
seBuyStrategy = se10dModel.rolling(window=2)\
    .apply(func=lambda x: x[0] == False and x[1] == True).fillna(0).astype(bool)  # type: Series
# 相邻节点滚动，找卖出拐点策略：均线由小于当日收盘变成大于
seSaleStrategy = se10dModel.rolling(window=2)\
    .apply(func=lambda x: x[0] == True and x[1] == False).fillna(0).astype(bool)  # type: Series

# 按照买入策略找买点的收盘价
dfBuy = dfStock[seBuyStrategy]
# 按照卖出策略找卖点的收盘价
dfSale = dfStock[seSaleStrategy]

# 模拟交易过程
# 本金10w
capital = 100000
# 余额，初始也是本金
balance = capital
# 可以买入的累计股数
buyTimes = len(dfBuy.index)
# 每次买入都砸进全部本金
for tradeNum in range(buyTimes):
    # 买入股数（假定该公司业务支持拆股，也就是说股数可以是小数）
    stockCount = balance / dfBuy.iloc[tradeNum]["close"]
    print(stockCount)
    # 卖出价格
    balance = stockCount * dfSale.iloc[tradeNum]["close"]
    # # 买入股数（如果不支持碎股，也就是说股数必须按整数算，我们照样有办法）
    # stockCount = balance // dfBuy.iloc[tradeNum]["close"]
    # # 剩余余额
    # balance -= stockCount * dfBuy.iloc[tradeNum]["close"]
    # # 卖出后，当前余额
    # balance = balance + stockCount * dfSale.iloc[tradeNum]["close"]

# 收益率
profitRate = (balance - capital) / capital

print(f"{buyTimes}次交易之后，收益率为{profitRate}")
