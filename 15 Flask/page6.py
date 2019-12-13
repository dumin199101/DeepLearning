# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/13 15:34
# 文件名称：page6
# 开发工具：PyCharm

# cookie session

from flask import Flask,make_response,request

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("cookie set success")
    resp.set_cookie("city","shenzhen")
    resp.set_cookie("name","wangjin")
    resp.set_cookie("age","22",max_age=3600)
    # resp.headers["Set-Cookie"] = "country=china; Expires=Fri, 13-Dec-2019 08:47:31 GMT; Max-Age=3600; Path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    return request.cookies.get("age")

@app.route("/del_cookie")
def del_cookie():
    resp = make_response("delete cookie")
    resp.delete_cookie("name")
    return resp


if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
