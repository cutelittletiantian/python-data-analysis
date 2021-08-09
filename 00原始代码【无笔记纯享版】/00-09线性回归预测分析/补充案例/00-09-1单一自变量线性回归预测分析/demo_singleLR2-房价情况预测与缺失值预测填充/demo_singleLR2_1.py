from sklearn.linear_model import LinearRegression
import pandas as pd
from pandas import DataFrame
import numpy

# 假设单一自变量为建筑面积，因变量为房屋价格，线性回归建模预测指定面积的房价
# 读取成都房源数据
df = pd.read_csv(filepath_or_buffer="成都市夜曲区房源数据.csv")  # type: DataFrame
# 清洗：null数据全部删除
df.dropna(axis=0, how="any", inplace=True)
# print(df.columns)
# Index(['房屋总价/万', '建筑面积', '房屋用途', '房屋户型'], dtype='object')

# 线性下降模型，并拟合面积-房价关系
lrModel = LinearRegression()
# 并拟合面积-房价关系
lrModel.fit(X=df[["建筑面积"]], y=df[["房屋总价/万"]])

# 拟合后，即可得到模型的系数和截距
# 系数
coefficient = lrModel.coef_[0, 0]  # type: numpy.ndarray
# 截距
intercept = lrModel.intercept_[0]  # type: numpy.ndarray

print(f"该线性回归模型为：y={coefficient}*x+{intercept}")

# 预测：房屋面积130的总价为XX万
pricePredict = lrModel.predict(X=[[130]])  # type: numpy.ndarray
print(f"房屋面积为130平方的总价为{pricePredict[0, 0]}万")
