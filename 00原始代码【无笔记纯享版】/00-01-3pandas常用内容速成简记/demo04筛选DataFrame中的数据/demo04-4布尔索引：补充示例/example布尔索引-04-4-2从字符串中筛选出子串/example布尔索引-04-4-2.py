import pandas as pd
from pandas import DataFrame, Series
from pandas.core.strings import StringMethods

# 资源文件
resourceFile = "信用卡用户信息.csv"

# 读入文件
dataFrame = pd.read_csv(filepath_or_buffer=resourceFile)

# print(dataFrame.columns)
# Index(['name', 'sex', 'ID_card', 'phone_number', 'email', 'company', 'career',
#        'credit_card_number', 'credit_limit', 'application_date', 'address'],
#       type='object')

# 布尔索引：性别为女
indexFemale = (dataFrame["sex"] == "F")
# 布尔索引：职业为其它
indexCareer = (dataFrame["career"] == "其他")
# 布尔索引：地址中包含四川
indexAddr = (dataFrame["address"].str.contains("四川"))

# 多条件筛选
result = dataFrame[indexFemale & indexCareer & indexAddr]
print(result)
