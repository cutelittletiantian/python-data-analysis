import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

# 配置坐标纸大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取营业额数据
df = pd.read_csv(filepath_or_buffer="resources/商场营业额数据.csv")
# print(df.columns)
# Index(['date', 'category', 'module', 'turnover'], dtype='object')

# 预处理：date字段转为日期
df["date"] = pd.to_datetime(arg=df["date"])

# 按照 业态 -> 模块 -> 月份 进行多级分组和重采样
dfByMonthlyCateModule = df.groupby(by=["category", "module"]).resample(on="date", rule="M").sum()  # type: DataFrame
# 取零售业态
dfRetail = dfByMonthlyCateModule.loc["零售"]  # type: DataFrame
# print(dfRetail.index)
# 商超、女装、电子产品、男装、童装

# 取零售业态下各模块
# 控制台查找知：行index为date，turnover为列名
# 商超模块
dfMarket = dfRetail.loc["商超"]  # type: DataFrame
# 女装模块
dfFemaleCloths = dfRetail.loc["女装"]  # type: DataFrame
# 电子产品模块
dfElecGadget = dfRetail.loc["电子产品"]  # type: DataFrame
# 男装模块
dfMaleCloths = dfRetail.loc["男装"]  # type: DataFrame
# 童装模块
dfKidCloths = dfRetail.loc["童装"]  # type: DataFrame

# 添加两行三列的子图
# 依次选择子图，并在上面绘制各模块的营业额数据
plt.subplot(2, 3, 1)
dfMarket.index = dfMarket.index.strftime("%Y/%m")
plt.bar(x=dfMarket.index, height=dfMarket["turnover"])
plt.xticks(rotation=90)
plt.title("商超")

plt.subplot(2, 3, 2)
dfFemaleCloths.index = dfFemaleCloths.index.strftime("%Y/%m")
plt.bar(x=dfFemaleCloths.index, height=dfFemaleCloths["turnover"])
plt.xticks(rotation=90)
plt.title("女装")

plt.subplot(2, 3, 3)
dfElecGadget.index = dfElecGadget.index.strftime("%Y/%m")
plt.bar(x=dfElecGadget.index, height=dfElecGadget["turnover"])
plt.xticks(rotation=90)
plt.title("电子产品")

plt.subplot(2, 3, 4)
dfMaleCloths.index = dfMaleCloths.index.strftime("%Y/%m")
plt.bar(x=dfMaleCloths.index, height=dfMaleCloths["turnover"])
plt.xticks(rotation=90)
plt.title("男装")

plt.subplot(2, 3, 5)
dfKidCloths.index = dfKidCloths.index.strftime("%Y/%m")
plt.bar(x=dfKidCloths.index, height=dfKidCloths["turnover"])
plt.xticks(rotation=90)
plt.title("童装")

# 防止遮挡布局
plt.tight_layout()
# 显示图像
plt.show()

# 将模块行索引出列，布局为行索引
dfRetail = dfRetail.unstack(level="module")

# 聚合
seriesTotalTurnover = dfRetail.sum(axis=1)

# 计算各模块站别
dfModulePercentage = dfRetail.apply(func=lambda item: item / seriesTotalTurnover)  # type: DataFrame
# index转换成"年-月"格式
dfModulePercentage.index = dfModulePercentage.index.strftime("%Y-%m")

# 绘制堆叠柱状图
dfModulePercentage.plot(kind="bar", stacked=True)

plt.show()