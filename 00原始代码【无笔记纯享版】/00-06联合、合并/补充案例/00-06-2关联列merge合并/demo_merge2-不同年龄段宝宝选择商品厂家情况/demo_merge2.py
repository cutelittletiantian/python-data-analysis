import pandas as pd
import matplotlib.pyplot as plt

# 分别读取商品、用户、订单的三个信息表
dfProduct = pd.read_csv(filepath_or_buffer="商品信息表.csv")
# 清洗空行空列
dfProduct.dropna(axis=0, inplace=True, how="all")
dfProduct.dropna(axis=1, inplace=True, how="all")
# print(dfProduct.columns)
# Index(['商品ID', '商品名', '单价', '厂家'], dtype='object')

dfUser = pd.read_csv(filepath_or_buffer="用户信息表.csv")
# 清洗空行空列
dfUser.dropna(axis=0, inplace=True, how="all")
dfUser.dropna(axis=1, inplace=True, how="all")
# print(dfUser.columns)
# Index(['用户ID', '地区', '宝宝性别', '宝宝年龄'], dtype='object')

dfOrder = pd.read_csv(filepath_or_buffer="订单信息表.csv")
# 清洗空行空列
dfOrder.dropna(axis=0, inplace=True, how="all")
dfOrder.dropna(axis=1, inplace=True, how="all")
# print(dfOrder.columns)
# Index(['订单号', '用户ID', '商品ID', '商品名', '单价', '数量', '总价', '下单时间'], dtype='object')

# 连接订单表-用户表-商品表，默认交集
dfBaby = pd.merge(left=dfOrder, right=dfUser).merge(right=dfProduct)
# print(dfBaby.columns)
# Index(['订单号', '用户ID', '商品ID', '商品名', '单价', '数量', '总价', '下单时间', '地区', '宝宝性别',
#        '宝宝年龄', '厂家'], dtype='object')

# 按 厂家 -> 年龄 进行分组，计数聚合
seriesBabyByFactoryAndAge = dfBaby.groupby(by=["厂家", "宝宝年龄"]).count()["订单号"]

# 拆出厂家这个索引为行索引
dfAgeFactory = seriesBabyByFactoryAndAge.unstack(level="厂家")

# 可视化年龄-厂家映射关系为百分比堆叠柱状图
# 配置坐标纸大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 转为百分比
dfAFPercentage = dfAgeFactory.apply(func=lambda item: item / dfAgeFactory.sum(axis=1))
# 绘制堆叠柱状
dfAFPercentage.plot(kind="bar", stacked=True)

# 调整子图布局
plt.tight_layout()
# 显示图像
plt.show()
