from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', get_category, name='category_list'),
    path('cat/create/', create_category, name='category-create'),
    path('cat/update/<int:pk>', update_category, name='category-update'),
    path('cat/delete/<int:pk>', delete_category, name='category-delete'),
    path('', get_products, name='product_list'),
    path('create/', add_product, name='product-add'),
    path('delete/<int:pk>', delete_product, name='product-delete'),
    path('update/<int:pk>', update_product, name='product-update'),

]
