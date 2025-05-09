

# Register your models here.
# store/admin.py
from django.contrib import admin
from .models import Book, Order

admin.site.register(Book)
admin.site.register(Order)
