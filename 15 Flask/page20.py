# *_* coding:utf-8 *_*
# 开发人员：烈焰
# 开发时间：2019/12/23 14:56
# 文件名称：page20
# 开发工具：PyCharm

# 单元测试
import unittest
from page19 import app
import json

class LoginTest(unittest.TestCase):
    """
    构造单元测试案例
    """
    def setUp(self):
        """
        在测试之前会被执行
        :return:
        """
        # 开启测试模式
        app.testing = True

        # 构造测试客户端
        self.client = app.test_client()

    def test_empty_username_password(self):
        """测试空用户名，空密码"""

        # 模拟发送web请求
        ret = self.client.post("/login",data={})
        # 获取响应体对象
        resp = json.loads(ret.data)
        # 拿到返回值进行测试
        self.assertIn("code",resp)
        self.assertEqual(resp["code"],0)

    def tearDown(self):
        """
        测试之后会执行
        :return:
        """
        print("测试完成！！！")

if __name__ == '__main__':
    unittest.main()







