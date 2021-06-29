import matplotlib.pyplot as plt
import pandas as pd

# 字体配置
plt.rcParams["font.sans-serif"] = "SimHei"
# 坐标纸张大小
plt.rcParams["figure.figsize"] = [12.8, 9.6]

# 读月销量数据
dfMonthSales = pd.read_csv("resources/书店每月销量数据.csv")
# 读销量-广告费数据
dfSalesAds = pd.read_csv("resources/书店图书销量和广告费用.csv")
# 读销量数据百分比数据
dfSalesPercentage = pd.read_csv("resources/书店每月销量数据百分比.csv")
# 读曝光-转化率数据
dfExConvert = pd.read_csv("resources/每月曝光量和转化率.csv")

# 使用plt.subplot(2, 2, x)函数添加4个子图，子图有两行两列

# 选择序号为1子图，绘制月销量波动折线图
plt.subplot(2, 2, 1)
# 绘制折线图，x轴为月份，y轴为总和
plt.plot(dfMonthSales["month"], dfMonthSales["sum"])
# 旋转x轴刻度，防止遮挡
plt.xticks(rotation=90)
# 将x轴标题设置为"月份"
plt.xlabel("月份")
# 将y轴标题设置为"销量"
plt.ylabel("销量")

# 选择序号为2子图，绘制广告和投入关联散点图
plt.subplot(2, 2, 2)
# 以df["ads_fee"]为x轴的值和df["sales"]为y轴的值，绘制散点图
plt.scatter(x=dfSalesAds["ads_fee"], y=dfSalesAds["sales"])
# 将x轴标题设置为"广告费用"
plt.xlabel("广告费用")
# 将y轴标题设置为"销量"
plt.ylabel("销量")

# 选择序号为3的子图，绘制不同楼层月销量的簇形柱状图（pandas辅助，可查文档）
plt.subplot(2, 2, 3)
# 簇形柱状图
# 查pandas文档，ax形参表示当前子图；查pandas文档，gca = get current axes
dfMonthSales.plot(
    kind="bar",
    x="month", y=["first_floor", "second_floor", "third_floor"],
    ax=plt.gca()
)
# 将x轴标题设置为"月份"
plt.xlabel("月份")
# 将y轴标题设置为"销量"
plt.ylabel("销量")

# 选择序号为4子图，绘制不同楼层月销量的堆叠柱状图（pandas辅助，可查文档）
plt.subplot(2, 2, 4)
# 百分比堆叠柱状图
dfSalesPercentage.plot(
    kind="bar", stacked=True,
    x="month", y=["一楼", "二楼", "三楼"],
    ax=plt.gca()
)
# 将x轴标题设置为"月份"
plt.xlabel("月份")
# 将y轴标题设置为"占比"
plt.ylabel("占比")

# 调整子图布局，避免图像之间互相遮挡
plt.tight_layout()
# 使用plt.show()函数显示图像
plt.show()
