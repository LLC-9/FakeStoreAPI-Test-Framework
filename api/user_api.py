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
        # 1. 加上伪装面具，假装是正常的谷歌浏览器，而不是没有感情的机器
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        response = requests.post(url, json=payload, headers=headers,proxies=self.proxies)

        if response.status_code not in [200,201]:
            print(f"警告：请求被拦截！状态码：{response.status_code}")
            print(f"服务器返回的内容：{response.text}")
            # 如果不是200或201，主动抛出异常，不让代码去强行解析 JSON
            raise Exception(f"API 请求失败，未能获取正确响应，状态码：{response.status_code}")

            # 3. 只有确保安全（状态码为 200）时，才去提取 token
        token = response.json()["token"]
        return token


if __name__ == '__main__':
    user = UserAPI()
    # 使用 FakeStoreAPI 提供的测试账号发起登录
    token = user.login("mor_2314", "83r5^_")
    print(f"成功拿到Token啦: {token}")