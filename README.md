# DeepLearning
机器学习&amp;深度学习&amp;数据分析

虚拟环境：

查看是否创建了虚拟环境：virtualenv --version

安装虚拟环境：1.pip install virtualenv 2.pip install virtualenvwrapper 

配置环境变量：

1.创建目录存放虚拟环境：mkdir $HOME/.virtualenvs

2.编辑~/.bashrc文件：

export WORKON_HOME = $HOME/.virtualenvs

source /usr/local/bin/virtualenvwrapper.sh

source ~/.bashrc

3.创建虚拟环境：

mkvirtualenv 虚拟环境名称

mkvirtualenv 虚拟环境名称 -p python3

4.安装工具包：

pip install flask==0.10.0

pip freeze > requirements.txt

pip install -r requirements.txt

5.启动虚拟环境：

workon 虚拟环境名称

6.退出当前虚拟环境：

deactivate

7.删除虚拟环境：

rmvirtualenv 虚拟环境名称

conda环境安装：

创建环境：conda create --name python3 python=3

切换环境：source activate python3

jupyter notebook:一款代替ipython的笔记软件

启动：jupyter notebook