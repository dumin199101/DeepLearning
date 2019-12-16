# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/16 15:16
# 文件名称：page10
# 开发工具：PyCharm

# flask-script扩展命令行

"""
python page10.py --help
positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Runs the Flask development server i.e. app.run()

python page10.py runserver -h 192.168.1.16 -p 6000
python page10.py shell
    In [1]: print(app)
        <Flask 'page10'>
    In [2]: print(app.url_map)
        Map([<Rule '/' (HEAD, GET, OPTIONS) -> index>,
     <Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>])
"""

from flask import Flask
from flask_script import Manager

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")
manager = Manager(app)

@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

if __name__ == '__main__':
    # 查看url路由
    #  print(app.url_map)
    #  app.run(port=5000)
    manager.run()
