# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/16 13:34
# 文件名称：page8
# 开发工具：PyCharm

# request session 请求上下文对象
# current_app g 应用上下文对象，current_app代表当前应用实例，g用于临时存储对象，每次请求会被重置

from flask import Flask,current_app,g

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

app.config["login"] = "login success!!!"

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/login")
def login():
    g.username = "hello world"
    data = say()
    return current_app.config.get("login") + data

def say():
    # 代替传参的方式
    return g.username + "!!!"



if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
