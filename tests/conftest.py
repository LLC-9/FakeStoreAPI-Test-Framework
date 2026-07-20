import pytest
from api.user_api import  UserAPI
from api.product_api import ProductAPI

@pytest.fixture(scope="session")
def get_token():
    print("执行唯一一次登录获取令牌")
    user = UserAPI()
    token = user.login("mor_2314", "83r5^_")
    return token

@pytest.fixture(scope="session")
def get_product():
    print("执行唯一一次查商品，获取ID")
    product = ProductAPI()
    t_product_id = product.get_all_products()[2]["id"]
    return t_product_id