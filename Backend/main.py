# Импортируем все что нам нужно
from fastapi import FastAPI, HTTPException
from typing import Optional, List
from datetime import date
import psycopg2
from pydantic import BaseModel


app = FastAPI()

# Модель пользователя
class User(BaseModel):
    id_user: int
    firstname: str
    surname: str
    mail: str
    phone: int
    address: str
    created_at: date
    rating: Optional[int]
    password: str

# Модель объявлений
class Ad(BaseModel):
    id_ad: int
    title: str
    text: str
    price: Optional[int]
    status: str
    address: str
    category_id: Optional[int]
    user_id: int
    created_at: date

# Модель категории
class Cathegory(BaseModel):
    id_cathegory: int
    title: str

# Модель заказа
class Order(BaseModel):
    id_order: int
    summ_order: float
    ad_id: int
    user_id: int

# Модель оценки
class Rating(BaseModel):
    id_rating: int
    rating: int
    comment: str
    ad_id: int

app = FastAPI()

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname = "avito",
    user = "postgres",
    password = "1234QWer",
    client_encoding = 'UTF8'
)
cur = conn.cursor()

# API для регистрации пользователей
@app.post("/User/registration/")
async def registration(userReg: User):
    query = "INSERT INTO \"User\" (firstname, surname, mail, password, phone, address, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_user"
    cur.execute(query, (userReg.firstname, userReg.surname, userReg.mail, userReg.password, userReg.phone, userReg.address, userReg.created_at))
    id_user = cur.fetchone()[0]
    conn.commit()
    return {"firstname": userReg.firstname, "surname": userReg.surname, "mail": userReg.mail, "password": userReg.password, "phone": userReg.phone, "address": userReg.address, "created_at": userReg.created_at}

# API Для логина пользователей
@app.post("/User/login/")
async def login(userLog: User):
    query = "SELECT id_user FROM \"User\" WHERE mail = %s AND password = %s"
    cur.execute(query, (userLog.mail,userLog.password))
    id_usergg = cur.fetchone()[0]
    conn.commit()
    if userLog.id_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return {"message": "User logged in succesfully", "id_user": id_usergg}

# API для просмотра объявлений пользователей по их внутреннему идентификатору
@app.get("/User/{user_id}/Ad/")
async def get_user_Ads(user_id: int):
    query = "SELECT id_ad, user_id, title, text, price, status, address, category_id, created_at FROM Ad WHERE user_id = %s"
    cur.execute(query, (user_id,))
    ads = cur.fetchall()
    return ads

# API для публикации новых объявлений
@app.post("/User/{user_id}/Ad/create_ad/")
async def create_Ad(user_id: int, AdCrt: Ad):
    query = "INSERT INTO ad (title, text, price, status, address, category_id, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_ad"
    cur.execute(query, (AdCrt.title, AdCrt.text, AdCrt.price, AdCrt.status, AdCrt.address, AdCrt.category_id, user_id, AdCrt.created_at))
    id_post = cur.fetchone()[0]
    conn.commit()
    return {"title": AdCrt.title, "text": AdCrt.text, "price": AdCrt.price, "status": AdCrt.status, "address": AdCrt.address, "category_id": AdCrt.category_id, "user_id": user_id, "created_at": AdCrt.created_at}

# API для редактирования объявлений
@app.put("/User/{user_id}/Ad/{id_ad}/redact/")
async def update_Ad(AdRed: Ad):
    query = "UPDATE Ad SET title = %s, text = %s, price = %s, status = %s, address = %s, category_id = %s WHERE id_ad = %s AND user_id = %s"
    cur.execute(query, (AdRed.title, AdRed.text, AdRed.price, AdRed.status, AdRed.address, AdRed.category_id, AdRed.id_ad, AdRed.user_id))
    conn.commit()
    return {"id_ad": AdRed.id_ad, "title": AdRed.title, "text": AdRed.text, "price": AdRed.price, "status": AdRed.status, "address": AdRed.address, "category_id": AdRed.category_id, "user_id": AdRed.user_id}

# API для удаления объявлений пользователей
@app.delete("/User/{user_id}/Ad/{id_ad}/")
async def delete_Ad(user_id: int, AdDel: Ad):
    query = "DELETE FROM Ad WHERE id_ad = %s AND user_id = %s"
    cur.execute(query, (AdDel.id_ad, user_id))
    conn.commit()
    return {"message": "Ad with id {} has been deleted".format(AdDel.id_ad)}

# API для добавления оценок по объявлениям
@app.post("/User/{user_id}/Rating/")
async def create_rating(ad_id: int, RatingCrt: Rating):
    query = "INSERT INTO rating (rating, comment, ad_id) VALUES (%s, %s, %s) RETURNING rating"
    cur.execute(query, (RatingCrt.rating, RatingCrt.comment, RatingCrt.ad_id))
    RatingCrt.id_rating = cur.fetchone()[0]
    conn.commit()
    return {"id_rating": RatingCrt.id_rating, "rating": RatingCrt.rating, "comment": RatingCrt.comment, "ad_id": RatingCrt.ad_id}

# API для просмотра оценок по их внутреннему идентификатору объявлений
@app.get("/User/{user_id}/Ad/Rating/")
async def get_user_ratings(ad_id: int):
    query = "SELECT * FROM rating WHERE ad_id = %s"
    cur.execute(query, (ad_id,))
    ratings = cur.fetchall()
    return ratings

# API для добавления заказов по объявлениям и пользователям
@app.post("/User/{user_id}/Order/")
async def create_order(ad_id: int, OrderCrt: Order):
    query = "INSERT INTO \"Order\" (summ_order, ad_id, user_id) VALUES (%s, %s, %s) RETURNING id_order"
    cur.execute(query, (OrderCrt.summ_order, OrderCrt.ad_id, OrderCrt.user_id))
    OrderCrt.id_order = cur.fetchone()[0]
    conn.commit()
    return {"id_order": OrderCrt.id_order, "summ_order": OrderCrt.summ_order, "ad_id": OrderCrt.ad_id, "user_id": OrderCrt.user_id}

# API для просмотра заказов по их внутреннему идентификатору пользователей
@app.get("/User/{user_id}/Ad/Order/")
async def get_user_orders(user_id: int):
    query = "SELECT * FROM \"Order\" WHERE user_id = %s"
    cur.execute(query, (user_id,))
    orders = cur.fetchall()
    return orders
