"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from users.views import login_page, logout_user
from article.views import home, add_to_category, list_of_category, add_to_article, list_of_product, get_one_product, delete_one_product, research_product, resupply_products

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),

    path('category/add/', add_to_category, name='addCategory'),
    path('category/', list_of_category, name='categories'),

    path('product/add/', add_to_article, name='addArticle'),
    path('product/', list_of_product, name='products'),

    path('product/<int:id>/', get_one_product, name='select_one_article'),
    path('delete/<int:id>/', delete_one_product, name='delete_one_article'),

    path('search/', research_product , name='search_view'),
    path('resupply/', resupply_products , name='resupply'),

]
