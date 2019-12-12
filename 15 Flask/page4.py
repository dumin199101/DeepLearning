# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/12 16:30
# 文件名称：page4
# 开发工具：PyCharm

# request对象

from flask import Flask,request

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/send",methods=["GET","POST"])
def send():
    name = request.form.get("name")
    age = request.form.get("age")
    city = request.args.get("city")
    return "hello name=%s,age=%s,city=%s" % (name,age,city)

@app.route("/upload",methods=["POST"])
def upload():
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "没有上传！"
    file_obj.save("1.png")
    return "上传成功"



if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
