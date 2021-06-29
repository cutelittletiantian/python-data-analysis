import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

# 字体配置
plt.rcParams["font.sans-serif"] = "SimHei"
# 坐标纸张大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]

# 读取excel表格
df = pd.read_excel(io="RFM.xlsx", sheet_name=0)  # type: DataFrame
# print(df.columns)
# Index(['品牌名称', '买家昵称', '付款日期', '订单状态', '实付金额', '邮费', '省份', '城市', '购买数量',
#        '下单次数'], dtype='object')

# 统计的截止时间
deadline = pd.to_datetime(arg="2020-10-1")

# 预处理：付款日期要稍作改动
df["付款日期"] = pd.to_datetime(arg=df["付款日期"])

# 按照买家做好分组
dfByCustomer = df.groupby(by="买家昵称")

# R标准：
# 统计的截止时间 - 每个买家的最近一次消费（付款日期最大值聚合），精确到天数
recency = (deadline - dfByCustomer.max()["付款日期"]).dt.days  # type: Series
# 均分2箱，前箱最近打1分，后箱距今远打0分
rankR = pd.qcut(x=recency, q=2, labels=[1, 0])  # type: Series
# 转为DataFrame类型，index重置，列名调整：买家昵称、R
rankR = rankR.to_frame(name="R").reset_index()  # type: DataFrame

# F标准
# 统计有消费的天数
frequency = dfByCustomer.count()["付款日期"]
# (0, 1]一箱，(1, 16]一箱，前箱子买的不勤快给0分，后箱子稍微活跃一点打1分
rankF = pd.cut(x=frequency, bins=[0, 1, 16], labels=[0, 1])  # type: Series
# 转为DataFrame类型，index重置，列名调整：买家昵称、F
rankF = rankF.to_frame(name="F").reset_index()  # type: DataFrame

# M标准
# 统计买家实付金额的总额
monetary = dfByCustomer.sum()["实付金额"]
# 均分2箱，前箱买的少打0分，后箱买的多打1分
rankM = pd.qcut(x=monetary, q=2, labels=[0, 1])  # type: Series
# 转为DataFrame类型，index重置，列名调整：买家昵称、M
rankM = rankM.to_frame(name="M").reset_index()  # type: DataFrame

# 组装RFM得分
rankRFM = rankR.merge(right=rankF, on="买家昵称").merge(right=rankM, on="买家昵称")

# 人群类型辨别
rankRFM["mark"] = rankRFM["R"].astype(dtype=str) + rankRFM["F"].astype(dtype=str) + rankRFM["M"].astype(dtype=str)
rankRFM["人群类型"] = rankRFM["mark"].apply(
    func=lambda seriesItem:
    "高价值用户" if seriesItem == "111" else
    "重点发展用户" if seriesItem == "101" else
    "重点唤回用户" if seriesItem == "011" else
    "重点潜力用户" if seriesItem == "001" else
    "一般潜力用户" if seriesItem == "110" else
    "一般发展用户" if seriesItem == "100" else
    "一般维系用户" if seriesItem == "010" else
    "低价值用户"
)
# 人群类型计数
calcRFM = rankRFM.groupby(by="人群类型").count()["mark"]
print(calcRFM)

# 可视化
plt.bar(x=calcRFM.index, height=calcRFM.values)
plt.show()
