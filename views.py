# Для этого проекта мы разработали методы API для регистрации, входа, создания объявления(с возможностью выбора категории),
# поиска объявлений по категориям и названию, добавления объявлений в заказ, создание отзыва с оценкой другому пользователю
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User, Ad, Category, Order, Rating
# from .serializer import UserSerializer, AdSerializer, CategorySerializer, OrderSerializer, RatingSerializer

# class UserRegistration(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = User.objects.get(email=email, password=password)
#         if user:
#             return Response('Login successful!', status=status.HTTP_200_OK)
#         else:
#             return Response('Login failed!', status=status.HTTP_400_BAD_REQUEST)

# class AdCreation(APIView):
#     def post(self, request):
#         serializer = AdSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AdSearch(APIView):
#     def get(self, request, category_id, title):
#         ads = Ad.objects.filter(category_id=category_id, title=title)
#         serializer = AdSerializer(ads, many=True)
#         return Response(serializer.data)

# class AddToOrder(APIView):
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AddRating(APIView):
#     def post(self, request):
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render  # Импортирование функции render из django.shortcuts
from rest_framework.views import APIView  # Импортирование класса APIView из rest_framework.views
from rest_framework.response import Response  # Импортирование класса Response из rest_framework.response
from rest_framework import status  # Импортирование модуля status из rest_framework
from .models import User, Ad, Category, Order, Rating  # Импортирование моделей User, Ad, Category, Order, Rating из текущего пакета
from .serializer import UserSerializer, AdSerializer, CategorySerializer, OrderSerializer, RatingSerializer  # Импортирование сериализаторов для моделей

class UserRegistration(APIView):  # Определение класса UserRegistration, наследующего APIView
    def post(self, request):  # Метод для обработки POST запроса
        serializer = UserSerializer(data=request.data)  # Инициализация сериализатора User
        if serializer.is_valid():  
            serializer.save()  # Сохранение данных в случае валидности
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Возвращение успешного ответа
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращение ошибки при невалидных данных

class UserLogin(APIView):  # Определение класса UserLogin, наследующего APIView
    def post(self, request):  # Метод для обработки POST запроса
        email = request.data.get('email')  # Получение email из запроса
        password = request.data.get('password')  # Получение пароля из запроса
        user = User.objects.get(email=email, password=password)  # Поиск пользователя с заданным email и паролем
        if user:
            return Response('Login successful!', status=status.HTTP_200_OK)  # Возвращение успешного ответа при успешном входе
        else:
            return Response('Login failed!', status=status.HTTP_400_BAD_REQUEST)  # Возвращение ошибки при неудачном входе

class AdCreation(APIView):  # Определение класса AdCreation, наследующего APIView
    def post(self, request):  # Метод для обработки POST запроса
        serializer = AdSerializer(data=request.data)  # Инициализация сериализатора Ad
        if serializer.is_valid():
            serializer.save()  # Сохранение данных в случае валидности
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Возвращение успешного ответа
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращение ошибки при невалидных данных

class AdSearch(APIView):  # Определение класса AdSearch, наследующего APIView
    def get(self, request, category_id, title):  # Метод для обработки GET запроса
        ads = Ad.objects.filter(category_id=category_id, title=title)  # Поиск объявлений по заданной категории и заголовку
        serializer = AdSerializer(ads, many=True)  # Сериализация найденных объявлений
        return Response(serializer.data)  # Возвращение данных об объявлениях

class AddToOrder(APIView):  # Определение класса AddToOrder, наследующего APIView
    def post(self, request):  # Метод для обработки POST запроса
        serializer = OrderSerializer(data=request.data)  # Инициализация сериализатора Order
        if serializer.is_valid():
            serializer.save()  # Сохранение данных в случае валидности
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Возвращение успешного ответа
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращение ошибки при невалидных данных

class AddRating(APIView):  # Определение класса AddRating, наследующего APIView
    def post(self, request):  # Метод для обработки POST запроса
        serializer = RatingSerializer(data=request.data)  # Инициализация сериализатора Rating
        if serializer.is_valid():
            serializer.save()  # Сохранение данных в случае валидности
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Возвращение успешного ответа
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращение ошибки при невалидных данных

