# 案例背景描述

某品牌旗舰店SW要通过构造RFM模型，观察用户标记分层的结果，有针对性地精细化运营，冲刺业绩。

* **R** 代表最近一次购买距今多少天

* **F** 代表购买了多少次

* **M** 代表购买总金额

# 数据表

* **RFM.xlsx**：买家消费情况数据表，字段如下

   * 品牌名称
     
   * 买家昵称
     
   * 付款日期
     
   * 订单状态
     
   * 实付金额
     
   * 邮费
     
   * 省份
     
   * 城市
     
   * 购买数量
     
   * 下单次数

# 分析标准

1. 所有的数据都按照“买家昵称”来分组（其实最标准的应该是用id，但是没办法数据有限只好用昵称），日期要全部做预处理，所有的分析截止日期为2020年10月1日

2. R值依据获取：选出各买家最近一次的付款日期，计算到分析截止日的天数。均分2组，分别标记1分和0分（天数约少最近的消费越近）

3. F值获取：各买家有购买日期的数据行数记个数。分(0, 1]和(1, 16]两个区间（单位：次），分别标记0分和1分（次数约高频率越高）

4. M值获取：将各买家的"实付金额"求和。分2组，分别标记0分和1分（取值越高金额越高）

5. 可视化，打印出RFM模型划分的9种买家人数情况

> RFM打分情况与买家分类对照

```python
# x代表的是RFM三个指标依次的标记分
if x == "111":
    "高价值用户"
elif x == "101":
    "重点发展用户"
elif x == "011":
    "重点唤回用户"
elif x == "001":
    "重点潜力用户"
elif x == "110":
    "一般潜力用户"
elif x == "100":
    "一般发展用户"
elif x == "010":
    "一般维系用户"
else:
    "低价值用户"
```