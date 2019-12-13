# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/13 17:38
# 文件名称：page7
# 开发工具：PyCharm

from flask import Flask
from flask import session

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")
app.config['SECRET_KEY'] = 'dfsafakjfdalsdf'

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return session.get('name')

@app.route("/login")
def login():
    session['name'] = 'wangliang'
    return "login success"

if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)