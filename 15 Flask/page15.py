# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/17 16:02
# 文件名称：page15
# 开发工具：PyCharm

# sqlalchemy:将模型类转换为sql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

# flask程序只认mysqlDB
pymysql.install_as_MySQLdb()

class Config(object):
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/python"
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 输出调试信息
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)
# 创建sqlalchemy对象
db = SQLAlchemy(app)

# 创建模型类
class Role(db.Model):
    __tablename__ = "tb_role"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    users = db.relationship("User",backref="role")

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer,db.ForeignKey("tb_role.id"))



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
    # 删除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()
