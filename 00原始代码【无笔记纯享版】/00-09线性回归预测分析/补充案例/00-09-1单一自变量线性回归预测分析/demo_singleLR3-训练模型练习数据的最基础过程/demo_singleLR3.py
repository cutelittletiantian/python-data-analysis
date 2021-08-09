import pandas as pd
from pandas import DataFrame
from matplotlib.axes import Axes
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy

# 用于预测的数据集的路径
testPath = "test.csv"
# 用于训练数据集的路径
trainPath = "train.csv"

# Step 1: 训练模型
# 读取训练数据集
dfTrain = pd.read_csv(filepath_or_buffer=trainPath)
# print(dfTrain.columns)
# Index(['x', 'y'], dtype='object')
# 建模：线性下降模型
lrModel = LinearRegression()
# 拟合
lrModel.fit(X=dfTrain[["x"]], y=dfTrain[["y"]])

# Step 2: 预测数据
# 读取预测数据集
dfTest = pd.read_csv(filepath_or_buffer=testPath)
# print(dfTest.columns)
# Index(['x', 'y'], dtype='object')
# 结合已经训练出来的模型，用x轴取值来预测y轴数据
yPredict = lrModel.predict(X=dfTest[["x"]])  # type: numpy.ndarray

# Step 3: 预测值和真实值对比可视化
plt.rcParams["font.sans-serif"] = "SimSun"
# plt.rcParams["figure.figsize"] = (12.8, 9.6)

fig, axes = plt.subplots(nrows=1, ncols=2)
# 预测值散点
curAx = axes[0]  # type: Axes
curAx.scatter(x=dfTest["x"], y=[item[0] for item in yPredict])
curAx.set_xlabel(xlabel="x")
curAx.set_ylabel(ylabel="y预测值")
curAx.set_title(label="预测值")
# 真实值散点
curAx = axes[1]  # type: Axes
curAx.scatter(x=dfTest["x"], y=dfTest["y"])
curAx.set_xlabel(xlabel="x")
curAx.set_ylabel(ylabel="y真实值")
curAx.set_title(label="真实值")
# 紧凑布局
plt.tight_layout()
# 输出
plt.show()
