import pandas as pd
import matplotlib.pyplot as plt

# excel工作簿写缓冲区
salesBookBuffer = pd.ExcelFile(path_or_buffer="202001.xlsx")

# 把所有的工作表数据都取出来（跳过第1个，已经读了）
df = pd.concat(objs=[pd.read_excel(io=salesBookBuffer, sheet_name=salesSheetName)
                     for salesSheetName in salesBookBuffer.sheet_names])
# 清洗掉全部为空的列和行（excel老传统艺能了）
df.dropna(axis="columns", how="all", inplace=True)
df.dropna(axis="index", how="all", inplace=True)
# print(df.columns)
# Index(['订单号', '商品名称', '商品单价', '商品数量', '商品总价', '优惠金额', '实付款', '下单时间', '发货时间'], dtype='object')

# 按照商品名称进行购买人次统计（不考虑单次买了多少个）
seriesCntByProduct = df["商品名称"].value_counts()

# 配置字体和图纸大小
plt.rcParams["font.sans-serif"] = ["SimSun"]
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 柱状图可视化购买人次
seriesCntByProduct.plot(kind="bar")
# 调整布局，显示图像
plt.tight_layout()
plt.show()
