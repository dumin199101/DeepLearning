# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/9/23 14:59
# 文件名称：matplotlib.py
# 开发工具：PyCharm
# matplotlib 绘制折线图
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf')

# 设置图片大小
plt.figure(figsize=(10, 6), dpi=80)
x = range(2, 26, 2)
y = [15, 13, 16, 11, 15, 22, 21, 14, 15, 12, 18, 13]
# 绘制折线图
plt.plot(x, y)
# 调整x轴刻度
plt.xticks(x)
# 设置标题
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度 单位（摄氏度）', fontproperties=my_font)
plt.title('一天气温变化图', fontproperties=my_font)
# 保存图片
# plt.savefig("./matplotlib.png")
plt.show()
