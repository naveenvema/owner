"""
URL configuration for owner project.

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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.customer_page, name='customer_page'),
    path('products_page', views.products_page, name='products_page'),
    path('Category_page', views.Category_page, name='Category_page'),
    path('Transactions', views.Transactions, name='Transactions'),
    path('category_create', views.category_create, name='category_create'),
    path('product_create', views.product_create, name='product_create'),
    path('customer_create/', views.customer_create, name='customer_create'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('customer_details/<int:id>', views.customer_details, name='customer_details'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),
    path('product_update/<int:id>', views.product_update, name='product_update'),
    path('successfully_updated/<int:id>', views.successfully_updated, name='successfully_updated'),
    path('successfully_updated_product/<int:id>', views.successfully_updated_product, name='successfully_updated_product'),
    path('Add_product_to_the_customer/<int:id>', views.Add_product_to_the_customer, name='Add_product_to_the_customer'),
     path('successfully_added_to_customer/<int:customer_id>/<int:product_id>', views.successfully_added_to_customer, name='successfully_added_to_customer'),
]
