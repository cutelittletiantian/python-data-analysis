import pandas as pd
from pandas import Series

df = pd.read_csv(filepath_or_buffer="电脑评分.csv")

# 清洗：order_id存在缺项
df.drop(
    index=df[df["order_id"].isnull()].index,
    inplace=True
)

# 按品牌分组、求均值
series_by_brand = df.groupby(["brand"])["rating"].mean()  # type: Series

print(series_by_brand)

# 格式化输出结果
print(f"各大平台"
      f"苹苹电脑平均评分为{series_by_brand['苹苹电脑']}，"
      f"华华电脑平均评分为{series_by_brand['华华电脑']}，"
      f"联联电脑平均评分为{series_by_brand['联联电脑']}，"
      f"惠惠电脑平均评分为{series_by_brand['惠惠电脑']}，"
      f"戴戴电脑平均评分为{series_by_brand['戴戴电脑']}，"
      f"硕硕电脑平均评分为{series_by_brand['硕硕电脑']}")
