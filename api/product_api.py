import requests
from api.base_api import BaseAPI

class   ProductAPI(BaseAPI):

    def get_all_products(self):
        """"获取所有商品列表接口"""
        url = f"{self.base_url}/products"
        response = requests.get(url,proxies= self.proxies)

        products_list = response.json()

        return products_list
if __name__ == "__main__":
    product = ProductAPI()
    product_get =  product.get_all_products()
    print(f"第三个商品：{product_get[2]['title']},价格:{product_get[2]['price']}")

