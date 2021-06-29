import pandas as pd
import matplotlib.pyplot as plt

# 配置图表尺寸
plt.rcParams["figure.figsize"] = [12.8, 9.6]
# 配置字体
plt.rcParams["font.sans-serif"] = "SimHei"

# 读取视频会员订单数据
df = pd.read_csv(filepath_or_buffer="视频会员订单数据.csv")
# print(df.columns)
# Index(['Unnamed: 0', 'order_id', 'user_id', 'price', 'platform', 'payment_provider', 'create_time', 'pay_time'],
#       dtype='object')

# 预处理：时间类型
df["create_time"] = pd.to_datetime(arg=df["create_time"])
df["pay_time"] = pd.to_datetime(arg=df["pay_time"])

# 支付时间-订单创建时间列添加进来
df["time_gap"] = df["pay_time"] - df["create_time"]

# 转换为“秒”
df["time_gap"] = df["time_gap"].dt.seconds

# 直方图绘制，x轴平均分成50组数据绘制
plt.hist(x=df["time_gap"], bins=50)

# 显示图像
plt.show()
