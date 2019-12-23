# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/23 15:42
# 文件名称：page22
# 开发工具：PyCharm

#单元测试之数据库测试

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

# flask程序只认mysqlDB
pymysql.install_as_MySQLdb()

class Config(object):
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/python3"
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 输出调试信息
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)
# 创建sqlalchemy对象
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(64))


