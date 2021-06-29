import pandas as pd
import matplotlib.pyplot as plt

# 读取脱发信息文件
df = pd.read_csv(filepath_or_buffer="2019年国内脱发人群抽样信息.csv")
# print(df.columns)
# Index(['性别', '年龄', '职业', '所在城市', '脱发类型'], dtype='object')

# 预处理：分组统计
# 统计不同性别人数
seriesGenderCnt = df["性别"].value_counts()
# 也可以按照SQL语句特色来分组、聚合
# 不过，这里需要添加代理码
# df["surrogate"] = df.index
# seriesGenderCnt = df.groupby(by="性别").count().sort_values(by="surrogate", ascending=False)["surrogate"]

# 统计不同年龄人数
seriesAgeCnt = df["年龄"].value_counts()
# 不同职业人数统计
seriesCareerCnt = df["职业"].value_counts()
# 所在不同城市人数统计
seriesCityCnt = df["所在城市"].value_counts()
# 不同脱发类型人数统计
seriesHairLossTypeCnt = df["脱发类型"].value_counts()

# 性别与最多脱发类型简报
print(f"本次抽样调查中男性脱发人数为{seriesGenderCnt['男']}，"
      f"女性脱发人数为{seriesGenderCnt['女']}，"
      f"脱发类型人数最多的为{seriesHairLossTypeCnt.idxmax()}")

# 数据可视化
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['figure.figsize'] = [12.8, 9.6]
# 绘制年龄——人数柱状图
plt.subplot(2, 2, 1)
plt.bar(x=seriesAgeCnt.index, height=seriesAgeCnt.values)
plt.xlabel(xlabel="年龄")
plt.ylabel(ylabel="人数")

# 绘制职业——人数柱状图
plt.subplot(2, 2, 2)
plt.bar(x=seriesCareerCnt.index, height=seriesCareerCnt.values)
plt.xlabel(xlabel="职业")
plt.ylabel(ylabel="人数")
plt.xticks(rotation=45)

# 绘制所在城市——人数柱状图
plt.subplot(2, 1, 2)
plt.bar(x=seriesCityCnt.index, height=seriesCityCnt.values)
plt.xlabel(xlabel="所在城市")
plt.ylabel(ylabel="人数")

# 调整子图布局
plt.tight_layout()
# 展示图片
plt.show()
