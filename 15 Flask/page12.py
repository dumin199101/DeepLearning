# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/17 13:57
# 文件名称：page12
# 开发工具：PyCharm

# 表单模型验证

from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__,static_url_path="/static",static_folder="static",template_folder="templates")

app.config['SECRET_KEY'] = 'sdfjsuogmnaslfgnadfvbsdf'

class LoginForm(FlaskForm):
    """登录表单模型验证"""
    user_name = StringField(label="登录名",validators=[DataRequired(message="登录名不能为空")])
    password = PasswordField(label="密码",validators=[DataRequired(message="密码不能为空")])
    password2 = PasswordField(label="确认密码",validators=[DataRequired(message="确认密码不能为空"),EqualTo("password",message="两次密码不一致")])
    submit = SubmitField(label="提交")


@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname,pwd,pwd2)
        session['username'] = uname
        return redirect(url_for('index'))
    else:
        return render_template("login.html",form=form)


@app.route("/index")
def index():
    """
    定义视图函数
    :return:
    """
    uname = session.get("username")
    return "Login name:%s" % uname

if __name__ == '__main__':
    # 查看url路由
     print(app.url_map)
     app.run(port=5000)
