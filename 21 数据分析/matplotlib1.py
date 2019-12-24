# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/24 16:17
# 文件名称：matplotlib1
# 开发工具：PyCharm

# 折线图：（变化）
# 直方图：（统计）绘制连续性数据（身高）
# 条形图：（统计）绘制离散性数据（苹果，香蕉）
# 散点图：（分布规律）两组数据间的对比

# matplotlib设置x轴刻度显示中文
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# 设置中文字体
my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")
# 设置图像大小
plt.figure(figsize=(10, 6), dpi=80)
# 准备数据
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
y2 = [random.randint(20, 35) for i in range(120)]
# 绘制数据
plt.plot(x, y, label="时间&气温", color="orange", linestyle="--")
plt.plot(x, y2, label="时间&气温2")
# 设置坐标轴信息
x_ticks = ["10点{}分".format(i) for i in range(60)]
x_ticks += ["11点{}分".format(i) for i in range(60)]
# 第二个参数为要替换的字符串，个数应该与第一个参数一致
plt.xticks(list(x)[::3], x_ticks[::3], rotation=45, fontproperties=my_font)
# 设置标题
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位（摄氏度）", fontproperties=my_font)
plt.title('10点到12点气温变化折现图', fontproperties=my_font)
# 设置图例
plt.legend(loc="upper right", prop=my_font)
# 显示
plt.show()
