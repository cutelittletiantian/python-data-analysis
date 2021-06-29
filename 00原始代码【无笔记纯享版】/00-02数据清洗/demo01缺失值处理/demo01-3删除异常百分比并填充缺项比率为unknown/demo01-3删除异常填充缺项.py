import pandas as pd
from pandas import DataFrame

df = pd.read_csv(filepath_or_buffer="WHO生育率数据.csv")  # type: DataFrame

# 查缺项数据
# df.info()

# 异常值删除：百分比大于100的比率，或者等于0（明显离谱的），或者小于0的要排除
df.drop(
    index=df[
        (df["Population_proportion_under_15"] > 100) |
        (df["Population_proportion_under_15"] <= 0)
        ].index,
    inplace=True
)
df.drop(
    index=df[
        (df["Population_proportion_over_60"] > 100) |
        (df["Population_proportion_over_60"] <= 0)
        ].index,
    inplace=True
)
df.drop(
    index=df[
        (df["Total_fertility_rate"] > 100) |
        (df["Total_fertility_rate"] <= 0)
        ].index,
    inplace=True
)

# 缺项数据默认unknown填入
df["Total_fertility_rate"].fillna(value="unknown", inplace=True)
# 检查是否还有缺项数据
df.info()
