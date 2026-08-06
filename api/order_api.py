import requests
from api.base_api import BaseAPI

class OrderAPI(BaseAPI):
    def __init__(self):
            super().__init__()

    def local_login(self):
        url = "http://127.0.0.1:8000/login"

        print(f"【DEBUG 调试】当前拼出来的登录请求地址是: {url}")

        response = requests.post(url, proxies=self.proxies)
        if response.status_code not in [200,201]:
            raise Exception(f"失败，状态码为:{response.status_code}")
        return response.json()['token']

    def create_order(self, token,product_id):
        url = "http://127.0.0.1:8000/order"
        headers = {
            "token": token
        }
        payload = {
            "product_id": product_id,
        }

        response = requests.post(url, headers=headers, json=payload,proxies=self.proxies)
        return response.status_code,response.json()


if __name__ == "__main__":
    print(f"本地测试开始")
    order_api = OrderAPI()
    order_token =  order_api.local_login()
    print(f"token:{order_token}")
    status_code, order_return = order_api.create_order(order_token,1)
    print(f"status_code:{status_code}")
    print(f"order_return:{order_return}")

