# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/10/10 11:09
# 文件名称：matplotlib3
# 开发工具：PyCharm
# matplotlib 绘制条形图
# 数据来源：www.58921.com
from matplotlib import pyplot as plt
from matplotlib import font_manager

x = ["战狼2", "哪吒之魔童降世", "流浪地球", "复仇者联盟4：终局之战", "红海行动", "美人鱼", "唐人街探案2", "我不是药神", "我和我的祖国", "中国机长"]
y = [56.39, 49.34, 46.18, 42.05, 36.22, 33.90, 33.71, 30.75, 30.62, 28.65]

my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf", size=30)
plt.figure(figsize=(40, 20), dpi=100)
plt.barh(range(len(x)), y, height=0.3)
# 将字符串设置到y轴
plt.yticks(range(len(x)), x, fontproperties=my_font)
plt.xticks(fontproperties=my_font)
plt.xlabel("总票房（亿元）", fontproperties=my_font)
plt.ylabel("电影名称", fontproperties=my_font)
# 设置网格
plt.grid(alpha=0.8)
plt.show()
