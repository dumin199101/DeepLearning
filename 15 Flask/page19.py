# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/23 14:42
# 文件名称：page19
# 开发工具：PyCharm

# 单元测试
# assert断言： assert 表达式 断言成功返回值为真，继续往下执行，否则断言失败

from flask import Flask,request,jsonify

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username,password]):
        resp = {
            "code":0,
            "message":"invalid request parameters"
        }
        return jsonify(resp)

    if username=="admin" and password=="123456":
        resp = {
            "code": 1,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "wrong username or wrong password"
        }
        return jsonify(resp)




if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
