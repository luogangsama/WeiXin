"""WeiXin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from sales.views import get_goods_info
from sales.views import add_car
from sales.views import get_carts_info
from sales.views import reduce

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sales/get_goods_info/', get_goods_info),
    path('api/sales/add_car/', add_car),
    path('api/sales/get_carts_info/', get_carts_info),
    path('api/sales/reduce/', reduce),
]
