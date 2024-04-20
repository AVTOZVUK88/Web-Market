"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.urls import re_path as url
# from backend_api.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', UserRegistration.as_view(), name='user-register'),
#     path('', UserLogin.as_view(), name='user-login'),
#     path('', AdCreation.as_view(), name='ad-create'),
#     path('', AdSearch.as_view(), name='ad-search'),
#     path('', AddToOrder.as_view(), name='order-add'),
#     path('', AddRating.as_view(), name='rating-add'),
# ]

from django.contrib import admin  # Импортируем модуль admin из django.contrib
from django.urls import path  # Импортируем функцию path из модуля django.urls
from django.urls import re_path as url  # Импортируем функцию re_path из модуля django.urls и предоставляем ей псевдоним url
from backend_api.views import *  # Импортируем все представления из backend_api.views

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для административной панели Django
    path('', UserRegistration.as_view(), name='user-register'),  # Путь для регистрации пользователя
    path('', UserLogin.as_view(), name='user-login'),  # Путь для входа пользователя
    path('', AdCreation.as_view(), name='ad-create'),  # Путь для создания объявления
    path('', AdSearch.as_view(), name='ad-search'),  # Путь для поиска объявлений
    path('', AddToOrder.as_view(), name='order-add'),  # Путь для добавления в заказ
    path('', AddRating.as_view(), name='rating-add'),  # Путь для добавления рейтинга
]