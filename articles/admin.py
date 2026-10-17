from django.contrib import admin
from .models import Article, Category, Product

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Product)