import pandas as pd

df = pd.read_csv(filepath_or_buffer="airData.csv")
# print(df.columns)
# ['member_no', 'ffp_date', 'first_flight_date', 'gender', 'ffp_tier',
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
#        'point_notflight']
# df.info()

# 清洗明显的异常值：第一年总票价（"sum_yr_1"）等于0，但总飞行公里数（"seg_km_sum"）大于0
df.drop(index=df[(df["sum_yr_1"] == 0) & (df["seg_km_sum"] > 0)].index, inplace=True)
# df.info()

# 类型转换：观测窗口结束时间（"load_time"）和入会时间（"ffp_date"）转时间类型
df["load_time"] = pd.to_datetime(arg=df["load_time"])
df["ffp_date"] = pd.to_datetime(arg=df["ffp_date"])
# df.info()
# 单独计算：入会时间
df["入会时间"] = df["load_time"] - df["ffp_date"]
# df.info()

# 为方便查找："flight_count"这一列重命名为"飞行次数"
df = df.rename(columns={"flight_count": "飞行次数"})
# df.info()

# 观察：入会时间和飞行次数这2列数据
print(df[["入会时间", "飞行次数"]])
