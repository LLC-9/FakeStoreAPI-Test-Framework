from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# 数据库初始化与造数据
def init_db():
    conn = sqlite3.connect("store.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, product_id INTEGER, user TEXT)")
    # 预置商品：测试手机，初始库存 10
    c.execute("INSERT OR IGNORE INTO products (id, name, stock) VALUES (1, 'TestPhone', 10)")
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