# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/20 16:09
# 文件名称：books.py
# 开发工具：PyCharm

from flask import Blueprint

app_book = Blueprint('app_book',__name__)

@app_book.route("/get_books")
def get_books():
    return "get_books pages"