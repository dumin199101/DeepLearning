# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/19 14:56
# 文件名称：page17
# 开发工具：PyCharm

# flask-migrage:数据库迁移，生成migrations文件夹
# 命令：init,migrate,upgrade,downgrade,history
# python page17.py db init
# python page17.py db migrate -m 'msg'
# python page17.py db upgrade
# python page17.py db history
# python page17.py db downgrade version

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

# flask程序只认mysqlDB
pymysql.install_as_MySQLdb()

class Config(object):
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/python2"
    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 输出调试信息
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)
# 创建sqlalchemy对象
db = SQLAlchemy(app)
# 创建flask脚本管理工具对象
manager = Manager(app)
# 创建数据库迁移工具对象
Migrate(app,db)
# 向manager中添加数据库操作命令
manager.add_command('db',MigrateCommand)

# 创建模型类
class Role(db.Model):
    __tablename__ = "tb_role"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    users = db.relationship("User",backref="role")

    def __repr__(self):
        """显示对象时更直观"""
        return self.name

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(64))
    city = db.Column(db.String(64))
    role_id = db.Column(db.Integer,db.ForeignKey("tb_role.id"))



@app.route("/")
def index():
    """
    定义视图函数
    :return:
    """
    return "Hello Python Flask!!"

if __name__ == '__main__':
    manager.run()

