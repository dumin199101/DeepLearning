# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/25 14:16
# 文件名称：matplotlib4
# 开发工具：PyCharm
# 绘制多条条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")

x = ["叶问4","误杀","只有云知道","星球大战：天行者崛起"]
y_22 = [9816,5451,1808,1677]
y_23 = [4288,2448,929,522]
y_24 = [5673,3756,1565,601]

bar_width = 0.3
x_22 = list(range(len(x)))
x_23 = [i+bar_width for i in x_22]
x_24 = [i+bar_width*2 for i in x_22]

plt.figure(figsize=(10,6),dpi=80)
plt.bar(x_22,y_22,width=bar_width,label="12月22日")
plt.bar(x_23,y_23,width=bar_width,label="12月23日")
plt.bar(x_24,y_24,width=bar_width,label="12月24日")

plt.xticks(x_23,x,fontproperties=my_font)

plt.legend(prop=my_font)

plt.show()