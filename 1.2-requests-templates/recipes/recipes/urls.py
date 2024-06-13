"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pip._internal import index

from views import all_home_view, calculate_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('recipes/',all_home_view, name='home'),
    path('recipes/<recipe_list>/',calculate_views, name='recipe_calculate'),
    # здесь зарегистрируйте вашу view-функцию
]
