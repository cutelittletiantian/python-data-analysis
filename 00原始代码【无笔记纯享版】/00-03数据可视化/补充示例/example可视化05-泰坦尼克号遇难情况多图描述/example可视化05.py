import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from pandas import DataFrame

# 配置图表尺寸
# plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = "SimHei"

# 读取泰坦尼克号遇难人员名单
dfTitanic = pd.read_csv(filepath_or_buffer="train.csv")  # type: DataFrame
# print(dfTitanic.columns)
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')

# 绘制2行2列复合图
fig, axes = plt.subplots(nrows=2, ncols=2)
# 人员存活情况子图
axSurvived = axes[0, 0]  # type: Axes
# 船舱等级子图
axPclass = axes[0, 1]  # type: Axes
# 性别子图
axGender = axes[1, 0]  # type: Axes
# 港口情况子图
axEmbarked = axes[1, 1]  # type: Axes

# 预处理
# 按幸存情况对人数分组计数
seriesSurvived = dfTitanic.groupby(by="Survived").count()["PassengerId"].sort_values(ascending=False)
# 按照船舱等级对人数分组计数
seriesPclass = dfTitanic.groupby(by="Pclass").count()["PassengerId"].sort_values(ascending=False)
# 按照性别对人数分组计数
seriesGender = dfTitanic.groupby(by="Sex").count()["PassengerId"].sort_values(ascending=False)
# 按照港口情况对人数分组计数
seriesEmbarked = dfTitanic.groupby(by="Embarked").count()["PassengerId"].sort_values(ascending=False)

# 绘制人员存活情况子图
axSurvived.bar(x=seriesSurvived.index.astype(dtype=str), height=seriesSurvived.values)
axSurvived.set_title(label="存活情况")
# x轴刻度旋转90度
for tickSurvived in axSurvived.get_xticklabels():
    tickSurvived.set_rotation(90)
axSurvived.set_ylabel(ylabel="人数")

# 绘制船舱等级情况子图
axPclass.bar(x=seriesPclass.index.astype(dtype=str), height=seriesPclass.values)
axPclass.set_title(label="船舱等级情况")
# x轴刻度旋转90度
for tickPclass in axPclass.get_xticklabels():
    tickPclass.set_rotation(90)
axPclass.set_ylabel(ylabel="人数")

# 绘制性别情况子图
axGender.bar(x=seriesGender.index, height=seriesGender.values)
axGender.set_title(label="性别")
# x轴刻度旋转90度
for tickGender in axGender.get_xticklabels():
    tickGender.set_rotation(90)
axGender.set_ylabel(ylabel="人数")

# 绘制性别情况子图
axEmbarked.bar(x=seriesEmbarked.index, height=seriesEmbarked.values)
axEmbarked.set_title(label="港口情况")
# x轴刻度旋转90度
for tickEmbarked in axEmbarked.get_xticklabels():
    tickEmbarked.set_rotation(90)
# 下面这个写法理论上可以，但是不推荐，因为set刻度标签本意是修改标签内容，所以每次都要重新指定x轴刻度标签，没必要
# axEmbarked.set_xticklabels(labels=seriesEmbarked.index, rotation=90)
axEmbarked.set_ylabel(ylabel="人数")

# 紧凑布局，防止互相遮挡
plt.tight_layout()
# 显示图像
plt.show()
