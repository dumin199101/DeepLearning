# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/17 15:33
# 文件名称：page14
# 开发工具：PyCharm

# flash闪现信息，存储在session中,第一次请求有效

from flask import Flask,flash,render_template

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

app.config['SECRET_KEY'] = 'sdjofjadgcvmxc,ngaotjer'

flag = True

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route('/flashed')
def flashed():
    global flag
    if flag:
        flash("hello")
        flash("world")
        flash("python")
        flag = False
    return render_template("flash.html")

if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)