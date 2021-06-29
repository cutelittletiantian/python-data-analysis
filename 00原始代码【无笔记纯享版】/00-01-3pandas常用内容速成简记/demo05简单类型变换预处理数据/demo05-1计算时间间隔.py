# 从datetime模块中导入datetime库（日期）
from datetime import datetime

# 构造一个2008年8月8日 20:08的时间
start = datetime(2008, 8, 8, 20, 8)
print(f"start = {start}")

# 构造一个2020年10月1日 10:00的时间
end = datetime(2020, 10, 1, 10)
print(f"end = {end}")

# 计算end减去start的差值，赋值给time_gap（表示时间间隔）
time_gap = end - start
print(time_gap)
# 时间间隔类型是datetime.timedelta
print(type(time_gap))
