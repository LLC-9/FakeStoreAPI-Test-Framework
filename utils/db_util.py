import sqlite3
import os


#创建连接库的类，定义连接到库的路径
class DButil():
    def __init__(self):
        root_path = os.path.dirname(os.path.dirname(__file__))
        self.db_path = os.path.join(root_path,"store.db")

#连接库
    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
#创建查询方法，使用查询的五个步骤,这里是查库存的办法
    def get_product_stock(self,product_id:int) -> int:
        #连接库
        conn = sqlite3.connect(self.db_path)
        #创建游标
        cursor = conn.cursor()
        #让游标执行数据库查询，使用元组传参?的方式保护库
        cursor.execute("SELECT stock FROM products WHERE id = ?",(product_id,))
        #取游标查询后返回的值
        row = cursor.fetchone()
        #关连接
        conn.close()
        #方法返回取到的值，这里因为取的是库存，可能会参与其他部分代码计算，所以不让他返回空值
        return row[0] if row else 0

    #以同样的方式创建取订单号的方法
    def get_product_order(self,product_id:int) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id,product_id,user FROM orders WHERE product_id = ? ORDER BY id DESC LIMIT 1",
            (product_id,))
        row = cursor.fetchone()
        conn.close()
        return row

        # 万能查询方法（专门为了测试断言准备的）
    def query(self, sql):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # 必须有这行，才能返回字典
        cursor = conn.cursor()

        cursor.execute(sql)
        row = cursor.fetchone()
        conn.close()

        return dict(row) if row else None

    #本地测试

if __name__ == "__main__":
    db = DButil()
    stock = db.get_product_stock(1)
    print(f"数据库测试，当前商品1的库存为{stock}")



