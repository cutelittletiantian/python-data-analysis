import pandas as pd
from pandas import DataFrame

# 探究价格与销量的关联系数
# 读取文件
df = pd.read_excel(io="自热火锅.xlsx", sheet_name=0)  # type: DataFrame
# print(df.columns)
# Index(['category', 'goods_name', 'shop_name', 'price', 'purchase_num', 'location'], dtype='object')

# 计算相关系数
corrPriceNum = df["price"].corr(other=df["purchase_num"])
print(corrPriceNum)
