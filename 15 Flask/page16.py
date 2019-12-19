# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/19 14:48
# 文件名称：page16
# 开发工具：PyCharm
from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

app.config.update(
    MAIL_SERVER = '',
    MAIL_USERNAME = '',
    MAIL_PASSWORD = '',
    MAIL_PORT = 465,
    MAIL_USE_TLS = True,
)

mail = Mail(app)



@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    # 邮件标题，发送者，接收者
    msg = Message(subject='',sender='',recipients=[])
    # 邮件内容
    msg.body = ''
    # 发送邮件
    mail.send(msg)
    return "Hello Python Flask!!"

if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
