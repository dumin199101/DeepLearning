# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/20 16:36
# 文件名称：__init__.py
# 开发工具：PyCharm

from flask import Blueprint

app_order = Blueprint('app_order',__name__,template_folder="templates")
# 让蓝图与应用知道视图的存在
from cart import views