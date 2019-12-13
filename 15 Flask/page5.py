# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/13 14:23
# 文件名称：abort
# 开发工具：PyCharm
# abort函数
from flask import Flask,request,abort,Response

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/login",methods=['POST','GET'])
def login():
    name = request.form.get('name','')
    pwd = request.form.get('pwd','')
    if name!='zhangsan' or pwd!='123456':
        # 返回标准状态码
        # abort(404)
        # 返回响应信息
        resp = Response('login failed')
        abort(resp)


if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
