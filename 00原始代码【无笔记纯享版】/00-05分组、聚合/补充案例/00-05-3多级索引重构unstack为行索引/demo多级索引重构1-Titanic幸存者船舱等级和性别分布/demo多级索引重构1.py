import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# 配置坐标纸大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = ["SimSun"]

# 读取泰坦尼克遇难者名单数据
dfTitanic = pd.read_csv(filepath_or_buffer="train.csv")
# print(dfTitanic.columns)
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')

# 按船舱等级分组，计算幸存率
seriesSurivedRateByPclass = \
    dfTitanic[dfTitanic["Survived"] == 1].groupby(by="Pclass")["Survived"].count() \
    / dfTitanic.groupby(by="Pclass")["Survived"].count()  # type: Series

# 按性别分组，计算幸存率
seriesSurivedRateByGender = \
    dfTitanic[dfTitanic["Survived"] == 1].groupby(by="Sex")["Survived"].count() \
    / dfTitanic.groupby(by="Sex")["Survived"].count()  # type: Series

# 1行2列复合子图
fig, ax = plt.subplots(nrows=1, ncols=2)

# 左图：船舱等级-幸存率 关系
axPclassSRate = ax[0]  # type: Axes
axPclassSRate.bar(x=seriesSurivedRateByPclass.index.astype(dtype=str),
                  height=seriesSurivedRateByPclass.values)
axPclassSRate.set_title(label="各船舱存活情况")
axPclassSRate.set_xlabel(xlabel="Pclass")
axPclassSRate.set_ylabel(ylabel="存活率")

# 右图：性别-幸存率 关系
axGenderSRate = ax[1]  # type: Axes
axGenderSRate.bar(x=seriesSurivedRateByGender.index,
                  height=seriesSurivedRateByGender.values)
axGenderSRate.set_title(label="各性别存活情况")
axGenderSRate.set_xlabel(xlabel="Sex")
axGenderSRate.set_ylabel(ylabel="存活率")

# 防止遮挡布局
plt.tight_layout()
# 显示图像
plt.show()
