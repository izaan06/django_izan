from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='products-list'),
    path('products/<slug:slug>/', views.product_detail, name='products-detail'),
    path('stores/', views.store_list, name='stores-list'),
    path('stores/<slug:slug>/', views.store_detail, name='stores-detail'),
    path('categories/', views.category_list, name='categories-list'),
    path('categories/<slug:slug>/', views.category_product_list, name='category-products'),
    path('prova404/', views.test_404, name='test-404'),
]
