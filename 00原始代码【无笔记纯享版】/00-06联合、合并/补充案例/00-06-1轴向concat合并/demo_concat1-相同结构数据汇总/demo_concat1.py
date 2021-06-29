import pandas as pd

# 为了突出汇总的代码，这里先不急着读取文件，先看原始数据
# 待汇总数据raw_data_1
raw_data_1 = {
        "project_id": ["1", "2", "3", "4", "5"],
        "first_name": ["Alex", "Amy", "Allen", "Alice", "Ayoung"],
        "last_name": ["Anderson", "Ackerman", "Ali", "Aoni", "Atiches"]}
# 待汇总数据raw_data_2
raw_data_2 = {
        "project_id": ["6", "7", "8", "9", "10"],
        "first_name": ["Billy", "Brian", "Bran", "Bryce", "Betty"],
        "last_name": ["Bonder", "Black", "Balwner", "Brice", "Btisan"]}

# 原始数据的DataFrame形式

# df1
# Out[3]:
#   project_id first_name last_name
# 0          1       Alex  Anderson
# 1          2        Amy  Ackerman
# 2          3      Allen       Ali
# 3          4      Alice      Aoni
# 4          5     Ayoung   Atiches
df1 = pd.DataFrame(data=raw_data_1)

# df2
# Out[4]:
#   project_id first_name last_name
# 0          6      Billy    Bonder
# 1          7      Brian     Black
# 2          8       Bran   Balwner
df2 = pd.DataFrame(data=raw_data_2)

# 垂直轴向合并（默认0）
dfAllVertical = pd.concat(objs=[df1, df2])

# 水平轴向合并
dfAllHorizontal = pd.concat(objs=[df1, df2], axis=1)

print(dfAllVertical)
print(dfAllHorizontal)
