from django.contrib import admin
from .models import Article, Category, Product, Review

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(Review)