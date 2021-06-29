import os
import pandas as pd

# 读取3月公交运营信息表
busBookBuffer = pd.ExcelFile(path_or_buffer="3月运营信息表.xlsx")

# 取出城市、乘客、订单工作表数据
dfSheetList = [pd.read_excel(io=busBookBuffer, sheet_name=sheetName) for sheetName in busBookBuffer.sheet_names]

# 城市工作表，乘客工作表，订单工作表
dfCity, dfPassenger, dfOrder = dfSheetList

# 按日期、城市连接三个工作表
dfBus = pd.merge(left=dfCity, right=dfPassenger, on=["日期", "城市"]) \
    .merge(right=dfOrder, on=["日期", "城市"])

# 月报路径
reportPath = "运营月报"
# 生成运营月报路径
if not os.path.exists(path=reportPath):
    os.mkdir(path=reportPath)
# 选出生成运营
dfBus[["日期", "城市", "订单呼叫次数", "订单应答数",
       "完成订单数", "订单应答率", "订单成交率",
       "新增呼叫乘客数", "新增呼叫乘客数", "新增激活司机数",
       "司机每日补贴", "乘客每日补贴"]].to_csv(path_or_buf=os.path.join(reportPath, "3月运营月报.csv"), index=False)
