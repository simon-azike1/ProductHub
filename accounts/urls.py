from django.urls import path
from .views import register_view, login_view, logout_view, product_list

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('products/', product_list, name='product_list'),
]
