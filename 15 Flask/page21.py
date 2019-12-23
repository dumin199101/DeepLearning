# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/23 15:28
# 文件名称：page21
# 开发工具：PyCharm
import unittest
from page22 import User,db,app

class DatabaseTest(unittest.TestCase):
    """
    数据库测试类
    """
    def setUp(self):
        """初始化"""
        app.testing = True
        db.create_all()

    def test_add_user(self):
        user = User(name="ma",email="123489034@qq.com",password="gfji2d")
        db.session.add(user)
        db.session.commit()

        result_user = User.query.filter_by(name="ma").first()
        self.assertIsNotNone(result_user)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()






