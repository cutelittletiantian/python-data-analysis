import pandas as pd

# 读工资表文件
df = pd.read_csv(filepath_or_buffer="公司员工工资表.csv")
# print(df.columns)
# Index(['name', 'salary', 'position'], dtype='object')

# 清洗：salary列中存在缺项，要处理掉
df.drop(inplace=True, index=df[df["salary"].isnull()].index)

# 工资的均值
meanSalary = df["salary"].mean()
# 工资的均中位数
medianSalary = df["salary"].median()
# 工资的众数
modeSalary = df["salary"].mode()[0]

print(f"公司员工的薪资的中位数为{medianSalary}元，均值为{meanSalary}元，众数为{modeSalary}元")
