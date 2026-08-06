from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import sqlite3
import os  # ！！！第1处修改：新增导入 os 模块！！！

app = FastAPI()

# ！！！第2处修改：动态获取项目根目录，并拼接出绝对路径！！！
root_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(root_path, "store.db")

# 数据库初始化与造数据
def init_db():
    # ！！！第3处修改：把原本的 "store.db" 替换为绝对路径 db_path ！！！
    conn = sqlite3.connect(db_path, check_same_thread=False)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, product_id INTEGER, user TEXT)")
    # 预置商品：测试手机，初始库存 99999
    c.execute("INSERT OR IGNORE INTO products (id, name, stock) VALUES (1, 'TestPhone', 99999)")
    conn.commit()
    return conn


conn = init_db()


class OrderReq(BaseModel):
    product_id: int


# 接口1：模拟登录获取Token
@app.post("/login")
def login():
    return {"token": "vip-token-888"}


# 接口2：下单接口（需Token校验 -> 查库存 -> 扣库存 -> 生成订单）
@app.post("/order")
def create_order(req: OrderReq, token: str = Header(None)):
    if token != "vip-token-888":
        raise HTTPException(status_code=401, detail="Unauthorized")

    c = conn.cursor()
    c.execute("SELECT stock FROM products WHERE id=?", (req.product_id,))
    row = c.fetchone()

    if not row or row[0] <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    # 模拟真实业务落库
    c.execute("UPDATE products SET stock = stock - 1 WHERE id=?", (req.product_id,))
    c.execute("INSERT INTO orders (product_id, user) VALUES (?, ?)", (req.product_id, "test_user"))
    conn.commit()

    return {"msg": "Order success", "order_id": c.lastrowid}