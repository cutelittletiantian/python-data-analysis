import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

# 字体配置
plt.rcParams["font.sans-serif"] = "SimHei"
# 坐标纸张大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]

# 加载B站up主稿件数据
dfBilibili = pd.read_csv(filepath_or_buffer="bilibili.csv")
# 清洗：空行
dfBilibili.dropna(axis=1)
# 预处理日期
dfBilibili["date"] = pd.to_datetime(arg=dfBilibili["date"])

# 初筛：分析视频上传个数>=5的up主
dfVideoCount = dfBilibili.groupby(by="author").count()["title"].reset_index()  # type: DataFrame
dfVideoCount.columns = ["author", "vid_count"]
dfVideoCount = dfVideoCount[dfVideoCount["vid_count"] >= 5]
# 内连接查询，选出>=5视频up主后，连接他们的其它视频数据信息
dfBilibili = dfVideoCount.merge(right=dfBilibili, on="author")
# 然后去掉vid_count，聚合之前这玩意是多余的
dfBilibili.drop(columns=["vid_count"], inplace=True)
# print(dfBilibili.columns)
# Index(['author', '分区', 'coins', 'danmu', 'favorite', 'likes',
#        'reply', 'share', 'view', 'title', 'date'], dtype='object')

# 按照up主，对数据进行分组
dfByAuthor = dfBilibili.groupby(by="author")

# 计算I指标
interactionRate = (dfByAuthor.sum()["danmu"] + dfByAuthor.sum()["reply"]) \
                  * 100 / dfByAuthor.sum()["view"] / dfByAuthor.count()["title"]
# 均分5箱，打分1~5，大于等于3分标记1，否则标记0
rankI = pd.qcut(x=interactionRate, q=5, labels=[1, 2, 3, 4, 5])  # type: Series
rankI = rankI.to_frame(name="I").reset_index()  # type: DataFrame

# 计算F指标
frequency = 1 / ((dfByAuthor.max()["date"] - dfByAuthor.min()["date"]).dt.days + 1) \
            * 100 / dfByAuthor.count()["title"]
# 均分5箱，打分1~5，大于等于3分标记1，否则标记0
rankF = pd.qcut(x=frequency, q=5, labels=[1, 2, 3, 4, 5])  # type: Series
rankF = rankF.to_frame(name="F").reset_index()  # type: DataFrame

# 计算L指标
loveRate = (dfByAuthor.sum()["likes"] + dfByAuthor.sum()["coins"] + dfByAuthor.sum()["favorite"]) \
           * 100 / dfByAuthor.sum()["view"]
# 均分5箱，打分1~5，大于等于3分标记1，否则标记0
rankL = pd.qcut(x=loveRate, q=5, labels=[1, 2, 3, 4, 5])  # type: Series
rankL = rankL.to_frame(name="L").reset_index()  # type: DataFrame

# 合成为IFL评分表，>=3分标记1，否则标记0
rankIFL = rankI.merge(right=rankF, on="author").merge(right=rankL, on="author")
rankIFL["I"] = rankIFL["I"].apply(func=lambda se_item: 1 if se_item > 3 else 0)
rankIFL["F"] = rankIFL["F"].apply(func=lambda se_item: 1 if se_item > 3 else 0)
rankIFL["L"] = rankIFL["L"].apply(func=lambda se_item: 1 if se_item > 3 else 0)

# 评分表汇总
rankIFL["mark"] = rankIFL["I"].astype(dtype=str) + rankIFL["F"].astype(dtype=str) + rankIFL["L"].astype(dtype=str)
# up主类型评价
rankIFL["authorCategory"] = rankIFL["mark"].apply(
    func=lambda se_item:
    "高质量UP主" if se_item == "111" else
    "高质量拖更UP主" if se_item == "101" else
    "高质量内容高深UP主" if se_item == "011" else
    "高质量内容高深拖更UP主" if se_item == "001" else
    "接地气活跃UP主" if se_item == "110" else
    "接地气UP主" if se_item == "100" else
    "活跃UP主" if se_item == "010" else "还在成长的UP主"
)

# 聚合统计不同分群up主人数
seCategory = rankIFL.groupby(by="authorCategory").count()["mark"]

# 可视化各类up主比例
plt.bar(x=seCategory.index, height=seCategory.values/seCategory.values.sum())
plt.xticks(rotation=45)
plt.show()
