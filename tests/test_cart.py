import pytest
from api.user_api import UserAPI
from api.cart_api import CarAPI
from api.product_api import ProductAPI
@pytest.mark.parametrize("quantity",[1,3,5])
def test_cart(quantity):
    "测试用例：用户成功将商品加入购物车"
    print(f"--当前数量为{quantity},测试开始--")

    #前置步骤,1、登录获取令牌，2、抓商品的id，3、调用购物车接口
    user = UserAPI()
    token = user.login("mor_2314","83r5^_")

    product = ProductAPI()
    t_product_id = product.get_all_products()[2]["id"]

    cart = CarAPI()
    status_codes,cart_result =  cart.add_to_cart(
        token=token,
        user_id=5,
        product_id=t_product_id,
        quantity=quantity
    )

    #使用断言，判断结果
    assert status_codes == 201

    assert "id"in cart_result

    print(f"数量为{quantity}的断言成功，状态码为{status_codes}")


