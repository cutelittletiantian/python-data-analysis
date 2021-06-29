import os
import pandas as pd

# 订单所在文件夹
salesPath = "历史月销售订单"
# 文件列表
salesItemList = os.listdir(path=salesPath)

# 汇总所有的文件
df = pd.concat(objs=[pd.read_csv(filepath_or_buffer=os.path.join(salesPath, salesItem))for salesItem in salesItemList])
# 清洗，清除全空列和全空行
df.dropna(axis=1, how="all", inplace=True)
df.dropna(axis=0, how="all", inplace=True)

# print(df.columns)
# Index(['订单号', '商品ID', '商品名', '品牌', '类别', '规格', '单价', '数量', '总价', '下单时间'], dtype='object')

# 预处理：订单号和商品ID全部都是字符串类型
df["订单号"] = df["订单号"].astype(dtype=str)
df["商品ID"] = df["商品ID"].astype(dtype=str)
print(df)

# 写进文件中，持久化结果
# if not os.path.exists(path="月销售订单汇总结果（不开源）"):
#     os.mkdir(path="月销售订单汇总结果（不开源）")
# # 写入csv文件
# df.to_csv(path_or_buf="月销售订单汇总结果（不开源）/2019-01至2020-10销售订单.csv", index=False)
# # 写入
# df.to_excel(excel_writer="月销售订单汇总结果（不开源）/2019-01至2020-10销售订单.xlsx", sheet_name="月销售汇总", index=False)
