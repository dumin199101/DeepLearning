# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/16 14:50
# 文件名称：page9
# 开发工具：PyCharm

#请求钩子:after_request,tear_down_request:携带请求参数response

"""
在第一次请求之前被调用
127.0.0.1 - - [16/Dec/2019 15:02:54] "GET / HTTP/1.1" 200 -
在请求之前被调用
在请求之后会被调用，前提是视图函数没有异常
在请求之后会被调用，不管视图函数有没有异常
"""

from flask import Flask

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.before_first_request
def before_first_request():
    """在第一次请求之前被调用"""
    print("在第一次请求之前被调用")

@app.before_request
def before_request():
    """在请求之前被调用"""
    print("在请求之前被调用")

@app.after_request
def after_request(response):
    """在请求之后被调用,前提是视图函数没有异常,携带response参数"""
    print("在请求之后会被调用，前提是视图函数没有异常")
    return response

@app.teardown_request
def tear_down_request(response):
    """在请求之后会被调用，不管视图函数有没有异常,携带response参数"""
    print("在请求之后会被调用，不管视图函数有没有异常")
    return response


if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
