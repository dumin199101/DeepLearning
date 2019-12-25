# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/25 15:02
# 文件名称：matplotlib5
# 开发工具：PyCharm
# matplotlib绘制直方图
from matplotlib import pyplot as plt

# 身高数据
# x = [167, 188, 199, 175, 198, 172, 160, 159, 163, 177, 176, 182, 182, 188, 172, 180, 188, 182, 192, 192, 188, 173,
#      171, 163, 159]

x = [100, 200, 150, 120, 110, 130, 130, 165, 185, 177, 179, 142, 184, 183, 181, 182, 193]

# 设置分成多少个组
width = 5
num = (max(x) - min(x)) // width
plt.xticks(list(range(min(x), max(x) + num, num)), rotation=45)
plt.grid(linestyle="-", alpha=0.5)
plt.hist(x, num)
# 显示频率
# plt.hist(x,num,normed=True)
plt.show()
