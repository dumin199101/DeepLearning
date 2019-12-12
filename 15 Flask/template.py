# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/12 15:18
# 文件名称：template.py
# 开发工具：PyCharm
from flask import Flask

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)