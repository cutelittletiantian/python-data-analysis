import pandas as pd
from pandas import DataFrame

# 资源文件：Titanic遇难者名单（简化版本），分析不同船舱的幸存率，清洗不是现在考虑的问题
resourceFile = "train.csv"

# 读出数据
dataFrame = pd.read_csv(filepath_or_buffer=resourceFile)

# print(dataFrame.columns)

# 计算3个船舱各自的幸存率
for noPclass in [1, 2, 3]:
    # 当前船舱的人员信息
    infoPclass = dataFrame[dataFrame["Pclass"] == noPclass]
    # 总人数
    totalCount = len(infoPclass.index)
    # print(totalCount)
    # 幸存人数
    survivedCount = infoPclass[infoPclass["Survived"] == 1].count()["PassengerId"]
    # 输出幸存率
    print(f"{noPclass}号船舱存活率是{survivedCount/totalCount}")
