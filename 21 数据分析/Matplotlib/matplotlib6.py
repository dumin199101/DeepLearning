# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/25 17:48
# 文件名称：matplotlib6
# 开发工具：PyCharm

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 将图表内容字体设置为黑体，可以正常显示中文

ratios = [0.1, 0.2, 0.15, 0.15, 0.4]  # 存放比例列表
colors = ['peru', 'coral', 'salmon', 'yellow', 'grey']  # 存放颜色列表，与比例相匹配
labels = ["流行", 'classic', 'pop', '纯音乐', 'blue']  # 存放各类元素标签
explode = (0, 0.1, 0, 0, 0.08) # 每一部分离开中心点的距离 ,元素数目与x相同且一一对应

plt.pie(ratios, explode=explode, colors=colors, labels=labels)  # 绘制饼图
plt.title('歌单音乐种类百分比')
plt.axis('equal')  # 将饼图显示为正圆形
plt.show()
