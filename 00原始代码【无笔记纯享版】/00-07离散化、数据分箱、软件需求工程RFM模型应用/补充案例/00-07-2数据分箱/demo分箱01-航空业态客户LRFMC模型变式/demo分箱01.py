import pandas as pd
from pandas import Series
from datetime import timedelta

# 航空公司的客户信息数据表

dfAirline = pd.read_csv(filepath_or_buffer="airData.csv")
# print(dfAirline.columns)
# Index(['member_no', 'ffp_date', 'first_flight_date', 'gender', 'ffp_tier',
#        'work_city', 'work_province', 'work_country', 'age', 'load_time',
#        'flight_count', 'bp_sum', 'ep_sum_yr_1', 'ep_sum_yr_2', 'sum_yr_1',
#        'sum_yr_2', 'seg_km_sum', 'weighted_seg_km', 'last_flight_date',
#        'avg_flight_count', 'avg_bp_sum', 'begin_to_first', 'last_to_end',
#        'avg_interval', 'max_interval', 'add_points_sum_yr_1',
#        'add_points_sum_yr_2', 'exchange_count', 'avg_discount',
#        'p1y_flight_count', 'l1y_flight_count', 'p1y_bp_sum', 'l1y_bp_sum',
#        'ep_sum', 'add_point_sum', 'eli_add_point_sum', 'l1y_eli_add_points',
#        'points_sum', 'l1y_points_sum', 'ration_l1y_flight_count',
#        'ration_p1y_flight_count', 'ration_p1y_bps', 'ration_l1y_bps',
#        'point_notflight'], dtype='object')

# 预处理，入会时间和观测窗口结束时间转时间类型
dfAirline["ffp_date"] = pd.to_datetime(arg=dfAirline["ffp_date"])
dfAirline["load_time"] = pd.to_datetime(arg=dfAirline["load_time"])

# 构造L指标，按照1个月30天估测
rankL = (dfAirline["load_time"] - dfAirline["ffp_date"]).dt.days / 30

# 按照频率分箱，分别打5 4 3 2 1分
seRankLbyFreq = pd.qcut(x=rankL, q=5, labels=[5, 4, 3, 2, 1])  # type: Series
# 大于3分的标记1，否则0
seRankLbyFreq = seRankLbyFreq.apply(func=lambda x: 1 if x > 3 else 0)

print(seRankLbyFreq)
