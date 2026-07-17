import requests

class   ProductAPI:
    def __init__(self):
        self.base_url = "https://fakestoreapi.com"

    def get_all_products(self):
        """"获取所有商品列表接口"""
        url = f"{self.base_url}/products"
        response = requests.get(url,proxies={"http":None,"https":None})

        products_list = response.json()

        return products_list
if __name__ == "__main__":
    product = ProductAPI()
    product_get =  product.get_all_products()
    print(f"第三个商品：{product_get[2]['title']},价格:{product_get[2]['price']}")

