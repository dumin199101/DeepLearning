# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/9/24 10:58
# 文件名称：matplotlib2
# 开发工具：PyCharm
# matplotlib 绘制散点图

from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf')

y_3 = [22, 12, 14, 14, 15, 22, 15, 18, 19, 24, 23, 25, 29, 33, 30, 31, 33, 29, 31, 28, 27, 26, 25, 25, 22, 28, 27, 26,
       23, 21, 22]
y_10 = [30, 31, 33, 29, 31, 28, 27, 26, 25, 25, 22, 28, 27, 26, 23, 21, 22, 22, 12, 14, 14, 15, 22, 15, 18, 19, 24, 23,
        25, 29, 33]

x_3 = range(1, 32)
x_10 = range(51, 82)

plt.figure(figsize=(10, 6), dpi=80)

plt.scatter(x_3, y_3, label='三月份')
plt.scatter(x_10, y_10, label='十月份')

_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i - 50) for i in x_10]
# 第一个参数设置原始数据，第二个参数设置字符串数据
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位（摄氏度）", fontproperties=my_font)
plt.title('三月份、十月份气温变化散点图', fontproperties=my_font)

# 设置图例
plt.legend(loc='upper left', prop=my_font)

plt.show()
