from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL-имя")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class Product(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб)")
    link = models.URLField(max_length=500, verbose_name="Партнёрская ссылка")

    def str(self):
        return self.name