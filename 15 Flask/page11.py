# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/16 15:39
# 文件名称：page11
# 开发工具：PyCharm

# 模板

from flask import Flask,render_template

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

@app.route("/book")
def book():
    data = {
      "name":"book2",
      "age":22,
      "list":[1,2,3,4,5],
      "str":"<script type='text/javascript'>alert('Hello')</script>"
    }
    # return render_template("book.html",name="book",age=22)
    return render_template("book.html",**data)


# 自定义注册过滤器
@app.template_filter("li22")
def li2(li):
    return li[::2]

app.add_template_filter(li2,"li2")


if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)


