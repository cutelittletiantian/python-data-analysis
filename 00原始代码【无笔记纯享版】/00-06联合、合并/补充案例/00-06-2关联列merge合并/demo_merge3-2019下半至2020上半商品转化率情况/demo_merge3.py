import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

# 配置坐标纸大小和字体
plt.rcParams["figure.figsize"] = [12.8, 9.6]
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 2019下半订单表
dfOrder2019 = pd.read_csv(filepath_or_buffer="2019年下半年订单表.csv")
# print(dfOrder2019.columns)
# Index(['订单号', '商品ID', '商品名', '单价', '数量', '总价', '下单时间'], dtype='object')

# 2020上半订单表
dfOrder2020 = pd.read_csv(filepath_or_buffer="2020年上半年订单表.csv")
# print(dfOrder2020.columns)
# Index(['订单号', '商品ID', '商品名', '单价', '数量', '总价', '下单时间'], dtype='object')

# 月浏览量表
dfExposure = pd.read_csv(filepath_or_buffer="Exposure.csv")
# print(dfExposure.columns)
# Index(['Month', 'ID', 'Exposure'], dtype='object')

# 轴向合并dfOrderxxxx，汇总
dfOrder = pd.concat(objs=[dfOrder2019, dfOrder2020])
# 预处理：下单时间转日期类型
dfOrder["下单时间"] = pd.to_datetime(arg=dfOrder["下单时间"])

# 按商品ID分组，按月频率采样
dfOrderMonthlyById = dfOrder.groupby(by="商品ID").resample(on="下单时间", rule="M").sum()[["数量"]]  # type: DataFrame
# 取消时间列索引
dfOrderMonthlyById.reset_index(inplace=True)
# 为了与月浏览量表时间连接，这里的时间要转化为年-月字符串格式
dfOrderMonthlyById["下单时间"] = dfOrderMonthlyById["下单时间"].dt.strftime(date_format="%Y-%m")

# 与浏览量Exposure表连接，关注["Month", "ID", "Exposure", "数量"]这几列
dfOrderExposure = pd.merge(left=dfOrderMonthlyById, right=dfExposure,
         left_on=["下单时间", "商品ID"], right_on=["Month", "ID"])[["Month", "ID", "Exposure", "数量"]]
# 预处理：商品ID是字符串也许比较适合
# dfOrderExposure["ID"] = dfOrderExposure["ID"].astype(dtype=str)

# 计算购买转化率
dfOrderExposure["购买转化率"] = dfOrderExposure["数量"] / dfOrderExposure["Exposure"]

# 可视化为折线图，2行3列
# 标题是对应商品的ID，"Month"为横坐标、"购买转化率"（保留2位小数）为纵坐标，图例为"转化率"，标记样式为"o"
# x轴刻度设置为90度，纵坐标范围为0-0.3
for graphCount, orderID in enumerate(list(set(dfOrderExposure["ID"].to_list())), start=1):
    plt.subplot(2, 3, graphCount)
    df = dfOrderExposure[dfOrderExposure["ID"] == orderID]
    plt.xticks(rotation=90)
    plt.ylim(0, 0.3)
    plt.plot(df["Month"], df["购买转化率"].round(2), marker="o", label="转化率")
    plt.legend()
    plt.title(orderID)

# # 按ID、月份分组
# dfOEByID = dfOrderExposure.groupby(by=["ID", "Month"]).sum()  # type: DataFrame
# # 添加列：购买转化率
# dfOEByID["购买转化率"] = dfOEByID["数量"] / dfOEByID["Exposure"]
# # 保留2位小数
# dfOEByID = dfOEByID.round(decimals=2)
# # 月份行转列索引，只留购买转化率
# dfOEByID = dfOEByID.unstack(level="Month")["购买转化率"]
#
# # 可视化为折线图，2行3列
# # 标题是对应商品的ID，"Month"为横坐标、"购买转化率"（保留2位小数）为纵坐标，图例为"转化率"，标记样式为"o"
# # x轴刻度设置为90度，纵坐标范围为0-0.3
# for graphNum, orderID in enumerate(dfOEByID.index.tolist(), start=1):
#     # 选子图
#     plt.subplot(2, 3, graphNum)
#     # 画图
#     dfOEByID.loc[orderID].plot(kind="line", y=dfOEByID.columns.tolist(), ylim=[0, 0.3],
#                                label="转化率", title=orderID, marker="o", xlabel="", rot=90)
#     # 显示图例
#     plt.legend()

# 调整布局
plt.tight_layout()
# 显示
plt.show()
