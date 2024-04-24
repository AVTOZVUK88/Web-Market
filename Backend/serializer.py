# Сериализаторы для наших API

# from rest_framework import serializers
# from .models import User, Ad, Category, Order, Rating

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class AdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad
#         fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         fields = '__all__'

from rest_framework import serializers  # Импортирование модуля serializers из rest_framework
from .models import User, Ad, Category, Order, Rating  # Импортирование моделей User, Ad, Category, Order, Rating из текущего пакета

class UserSerializer(serializers.ModelSerializer):  # Определение сериализатора User
    class Meta:  # Начало определения метакласса
        model = User  # Указание модели, с которой работает сериализатор
        fields = '__all__'  # Указание всех полей модели для сериализации

class AdSerializer(serializers.ModelSerializer):  # Определение сериализатора Ad
    class Meta:  # Начало определения метакласса
        model = Ad  # Указание модели, с которой работает сериализатор
        fields = '__all__'  # Указание всех полей модели для сериализации

class CategorySerializer(serializers.ModelSerializer):  # Определение сериализатора Category
    class Meta:  # Начало определения метакласса
        model = Category  # Указание модели, с которой работает сериализатор
        fields = '__all__'  # Указание всех полей модели для сериализации

class OrderSerializer(serializers.ModelSerializer):  # Определение сериализатора Order
    class Meta:  # Начало определения метакласса
        model = Order  # Указание модели, с которой работает сериализатор
        fields = '__all__'  # Указание всех полей модели для сериализации

class RatingSerializer(serializers.ModelSerializer):  # Определение сериализатора Rating
    class Meta:  # Начало определения метакласса
        model = Rating  # Указание модели, с которой работает сериализатор
        fields = '__all__'  # Указание всех полей модели для сериализации
