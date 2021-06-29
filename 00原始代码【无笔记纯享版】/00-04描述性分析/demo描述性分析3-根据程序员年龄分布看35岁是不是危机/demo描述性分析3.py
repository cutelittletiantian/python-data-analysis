import pandas as pd
import matplotlib.pyplot as plt

# 读取成都程序员有关数据
df = pd.read_csv(filepath_or_buffer="成都市程序员抽样信息.csv")
# print(df.columns)
# Index(['性别', '年龄', '薪资', '细分职业', '公司融资轮次'], dtype='object')

# 清洗年龄缺项
df.drop(inplace=True, index=df[df["年龄"].isnull()].index)

# 简报35岁以上程序员比例
print(f"35岁以上程序员所占比例为"
      f"{df[df['年龄'] > 35]['年龄'].count() / df['年龄'].count()}")

# 最值和四分位值描述
print(df["年龄"].describe())

# 数据可视化：各年龄人员数量构成
# 使用value_counts()函数，计算df里不同年龄的人数，并赋值给变量ageCount
ageCount = df["年龄"].value_counts()
# 配置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制年龄——人数饼状图
plt.pie(x=ageCount.values, labels=ageCount.index)
plt.show()
