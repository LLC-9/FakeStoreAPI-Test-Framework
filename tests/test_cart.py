import pytest
import yaml

from api.cart_api import CarAPI
from utils.utils_cart_quantities import utils_cart_quantities

yaml_quantities = utils_cart_quantities("data/cart.yaml")
@pytest.mark.parametrize("quantity",yaml_quantities["cart_quantities"])
def test_cart(quantity,get_token,get_product):
    "测试用例：用户成功将商品加入购物车"
    print(f"--当前数量为{quantity},测试开始--")

    cart = CarAPI()
    status_codes,cart_result =  cart.add_to_cart(
        token=get_token,
        user_id=5,
        product_id=get_product,
        quantity=quantity
    )

    #使用断言，判断结果
    assert status_codes == 201

    assert "id" in cart_result

    print(f"数量为{quantity}的断言成功，状态码为{status_codes}")


