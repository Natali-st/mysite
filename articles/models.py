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
    title = models.CharField(max_length=200)
    text = models.TextField()

    # Вот наши две картинки
    image_before = models.ImageField(upload_to='articles_images/', blank=True, null=True, verbose_name="Фото ДО")
    image_after = models.ImageField(upload_to='articles_images/', blank=True, null=True, verbose_name="Фото ПОСЛЕ")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, verbose_name="Лайки")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг") # <-- НОВАЯ СТРОКА
    
    def str(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ваше имя")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"Отзыв от {self.name}"

class Product(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='products', null=True, blank=True) # добавил null=True, чтобы товар мог существовать без статьи (для главной страницы)
    name = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб)")
    link = models.URLField(max_length=500, verbose_name="Партнёрская ссылка")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Фото товара") # <-- НОВАЯ СТРОКА