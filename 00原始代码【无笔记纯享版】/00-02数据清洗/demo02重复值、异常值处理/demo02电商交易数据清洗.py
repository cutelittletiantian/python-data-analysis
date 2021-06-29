import os
import pandas as pd

# 预备清洗结果的文件夹
resultPath = "cleaned"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)

# 待处理文件名
uncleandFile = "180101-190630交易数据.csv"
# 读取文件
df = pd.read_csv(filepath_or_buffer=uncleandFile)
# print(df.columns)
# df.info()

# 预处理：id为行索引
# 查重，无异常
# print(df["id"].duplicated())
df = df.set_index(keys="id")
# print(df)

# 预处理：create_time和pay_time转为datetime类型
df["create_time"] = pd.to_datetime(arg=df["create_time"])
# print(df["create_time"])
df["pay_time"] = pd.to_datetime(arg=df["pay_time"])
# print(df["pay_time"])

# 预处理：payment，price，cutdown_price，post_fee现在是以分为单位的，转化为元
df[["payment", "price", "cutdown_price", "post_fee"]] = df[["payment", "price", "cutdown_price", "post_fee"]] / 100
# print(df[["payment", "price", "cutdown_price", "post_fee"]])

# user_id，不存在<=0的异常值
df.drop(index=df[df["user_id"] <= 0].index, inplace=True)
# df.info()

# 时间异常值清洗：create_time不可能后于pay_time
df.drop(
    index=df[df["create_time"] > df["pay_time"]].index,
    inplace=True
)
# df.info()

# payment，price，cutdown_price，post_fee去掉<0这种不可能存在的异常值
df.drop(index=df[df["payment"] < 0].index, inplace=True)
df.drop(index=df[df["price"] < 0].index, inplace=True)
df.drop(index=df[df["cutdown_price"] < 0].index, inplace=True)
df.drop(index=df[df["post_fee"] < 0].index, inplace=True)
# df.info()

# items_count，不存在<0的异常值
df.drop(index=df[df["items_count"] < 0].index, inplace=True)
# df.info()

# order_id，不存在<=0的异常值，不存在重复值
# 异常值去除，然后再去重
df.drop(index=df[df["order_id"] <= 0].index, inplace=True)
df.drop(index=df[df["order_id"].duplicated()].index, inplace=True)
df.info()

# print(df)

# 保存清洗完成的文件
df.to_csv(path_or_buf=os.path.join(resultPath, f"【已清洗】{uncleandFile}"))
