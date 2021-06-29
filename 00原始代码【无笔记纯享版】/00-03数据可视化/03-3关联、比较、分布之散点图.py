import pandas as pd
import matplotlib.pyplot as plt

# 配置字体
plt.rcParams["font.sans-serif"] = "simhei"

# 读取文件
df = pd.read_csv(filepath_or_buffer="resources/书店图书销量和广告费用.csv")
# print(df.columns)
# Index(['date', 'sales', 'ads_fee', 'Unnamed: 3', 'Unnamed: 4'], dtype='object')

# 广告费用与销量的散点图
# 颜色设置为绿色
plt.scatter(
    df["ads_fee"], df["sales"],
    color="green"
)

# x轴和y轴图标
plt.xlabel(xlabel="广告费用")
plt.ylabel(ylabel="销量")

# 显示图像
plt.show()
