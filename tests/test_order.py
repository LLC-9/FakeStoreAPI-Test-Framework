import pytest
import allure
from api.order_api import OrderAPI
from utils.db_util import DButil

@allure.epic("本地Mock靶场核心业务")
@allure.feature("订单链路数据库自动化测试")
class TestOrder:
    def setup_class(self):
        """用例前置准备"""
        self.order_api = OrderAPI()
        self.db = DButil()
        self.token = self.order_api.local_login()

   # """因调用数据库方法里有弄关闭连接，所以不需要收尾工作断开数据库连接了""""
    # def teardown_class(self):
    #     """收尾工作"""
    #     self.db.close()

    @allure.story("创建订单并验证数据库")
    def test_create_order_success(self):
        product_id = 1

        with allure.step(f"步骤1：携带 Token 和商品ID({product_id})，调用下单接口"):
            status_code, response = self.order_api.create_order(self.token,product_id)

        with allure.step("步骤2：第一重断言 -> 校验 API 响应状态码及返回信息"):
            assert status_code in [200,201]
            assert response["msg"] == "Order success"
            order_id = response["order_id"]

        with allure.step(f"步骤3：第二重断言 -> 拿着接口返回的订单ID({order_id})去查询底层 SQLite 数据库"):
            sql = f"SELECT product_id FROM orders WHERE id={order_id}"
            db_result = self.db.query(sql)

            assert db_result is not None,"严重 Bug：接口返回成功，但数据库未生成订单！(若断言失败会出现这段中文，否则则不会)"
            assert db_result["product_id"] == product_id