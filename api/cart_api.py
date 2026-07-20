import requests
from api.base_api import BaseAPI

#创建加入购物车的类
class CarAPI(BaseAPI):
    def add_to_cart(self,token,user_id,product_id,quantity):
        url = f"{self.base_url}/carts"
        headers ={
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "userId": user_id,
            "date":"2026-07-17",
            "products":[
            {"productId":product_id,"quantity":quantity}
        ]
      }
#发送请求接口返回数据
        response = requests.post(url, json=payload, headers=headers,proxies=self.proxies)
        return response.status_code,response.json()
#测试
if __name__ == '__main__':
        from user_api import UserAPI
        from product_api import ProductAPI

        print(f"---测试---")
        #调用登录测试接口，接收token并存储
        user = UserAPI()
        token = user.login("mor_2314","83r5^_")
        print(f"密钥为:{token}")
        #调用商品列表查看接口，接收商品id
        product = ProductAPI()
        t_product_id =  product.get_all_products()[2]["id"]
        print(f"商品id为:{t_product_id}")
        #调用测试加入购物车接口
        cart = CarAPI()
        status_code, cart_result = cart.add_to_cart(token=token,user_id=5,product_id=t_product_id,quantity=1)

        print(f"状态码为:{status_code}\n,返回结果为：\n{cart_result}")

