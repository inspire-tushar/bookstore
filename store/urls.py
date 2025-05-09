from django.urls import path
from .views import order_book

urlpatterns = [
    path('order/', order_book, name='order_book'),
]
