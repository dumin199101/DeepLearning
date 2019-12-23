# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/23 13:55
# 文件名称：orders.py
# 开发工具：PyCharm

from cart import app_order
from flask import render_template

@app_order.route("/get_orders")
def get_orders():
    # return "get_orders pages"
    return render_template('orders.html')
