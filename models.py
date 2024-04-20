# У нас есть проект веб-сайта по типу авито, разработку мы ведем на react + djago, наши модели : 
# Пользователь (id, имя, фамилия, электрорнная почта, телефон, адрес, дата регистрации, id оценки), 
# Объявление(id, заголовок, описание, цена, дата размещения, состояние, адрес, id категории, id пользователя), 
# Категории (id, название, id  объявления), 
# Заказ (id, сумма, id объявления, id пользователя), 
# Оценка(id, оценка, комментарий, id объявления)

# from django.db import models

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     registration_date = models.DateField()
#     rating_id = models.IntegerField()

# class Ad(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     posting_date = models.DateField()
#     condition = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     category_id = models.IntegerField()
#     user_id = models.IntegerField()

# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     ad_id = models.IntegerField()

# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     ad_id = models.IntegerField()
#     user_id = models.IntegerField()

# class Rating(models.Model):
#     id = models.AutoField(primary_key=True)
#     rating = models.IntegerField()
#     comment = models.TextField()
#     ad_id = models.IntegerField()

from django.db import models  # Импортирование модуля models из django.db

class User(models.Model):  # Определение модели User
    id = models.AutoField(primary_key=True)  # Поле для уникального идентификатора пользователя
    first_name = models.CharField(max_length=50)  # Поле для имени пользователя
    last_name = models.CharField(max_length=50)  # Поле для фамилии пользователя
    email = models.EmailField()  # Поле для адреса электронной почты пользователя
    phone = models.CharField(max_length=20)  # Поле для номера телефона пользователя
    address = models.CharField(max_length=100)  # Поле для адреса пользователя
    registration_date = models.DateField()  # Поле для даты регистрации пользователя
    rating_id = models.IntegerField()  # Поле для идентификатора рейтинга пользователя

class Ad(models.Model):  # Определение модели Ad
    id = models.AutoField(primary_key=True)  # Поле для уникального идентификатора объявления
    title = models.CharField(max_length=100)  # Поле для заголовка объявления
    description = models.TextField()  # Поле для описания объявления
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для цены объявления
    posting_date = models.DateField()  # Поле для даты размещения объявления
    condition = models.CharField(max_length=20)  # Поле для состояния объявления
    address = models.CharField(max_length=100)  # Поле для адреса объявления
    category_id = models.IntegerField()  # Поле для идентификатора категории объявления
    user_id = models.IntegerField()  # Поле для идентификатора пользователя объявления

class Category(models.Model):  # Определение модели Category
    id = models.AutoField(primary_key=True)  # Поле для уникального идентификатора категории
    name = models.CharField(max_length=50)  # Поле для названия категории
    ad_id = models.IntegerField()  # Поле для идентификатора объявления категории

class Order(models.Model):  # Определение модели Order
    id = models.AutoField(primary_key=True)  # Поле для уникального идентификатора заказа
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для суммы заказа
    ad_id = models.IntegerField()  # Поле для идентификатора объявления в заказе
    user_id = models.IntegerField()  # Поле для идентификатора пользователя заказа

class Rating(models.Model):  # Определение модели Rating
    id = models.AutoField(primary_key=True)  # Поле для уникального идентификатора рейтинга
    rating = models.IntegerField()  # Поле для рейтинга
    comment = models.TextField()  # Поле для комментария к рейтингу
    ad_id = models.IntegerField()  # Поле для идентификатора объявления, к которому привязан рейтинг
