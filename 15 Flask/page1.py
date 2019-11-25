# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/11/25 11:03
# 文件名称：page1
# 开发工具：PyCharm

# 第一个Flask小程序
from flask import Flask,current_app

# __name__代表当前模块的名字，flask以这个模块所在的目录为总目录，以这个目录中的static为静态目录，templates为模板目录
# 当前启动文件：__name__就是__main__,否则就是模块名字
# Flask初始化参数：static_url_path,static_folder,template_folder
app = Flask(__name__,static_url_path="/python",static_folder="static",template_folder="templates")

# 加载配置文件
# 1.使用配置文件方式
app.config.from_pyfile("config.cfg")

# 2.使用对象方式
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)


#3.使用字典方式
# app.config["DEBUG"] = True

# 读取配置
print(app.config.get("HOST"))


@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    # a = 1 / 0
    print(current_app.config.get("HOST"))
    return "Hello Python Flask!!"

if __name__ == '__main__':
     app.run(port=5002)
