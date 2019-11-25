# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/25 16:01
# 文件名称：page2
# 开发工具：PyCharm

# Flask 路由
from flask import Flask,redirect,url_for

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"


@app.route("/hello",methods=["POST"])
def hello():
    return "Hello World"

@app.route("/say",methods=["POST"])
def say1():
    return "say1"

@app.route("/say")
def say2():
    return "say2"

@app.route("/eating")
@app.route("/eated")
def eat():
    return "eat"

@app.route("/go")
def go():
    # 反解析
    url = url_for("index")
    return redirect(url)


if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5003)

