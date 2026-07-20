import requests
from api.base_api import BaseAPI


class UserAPI(BaseAPI):

    def login(self, username, password):
        """用户登录接口"""
        url = f"{self.base_url}/auth/login"
        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(url, json=payload, proxies=self.proxies)

        token = response.json()["token"]

        return token


if __name__ == '__main__':
    user = UserAPI()
    # 使用 FakeStoreAPI 提供的测试账号发起登录
    token = user.login("mor_2314", "83r5^_")
    print(f"成功拿到Token啦: {token}")