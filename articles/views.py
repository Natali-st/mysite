from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request, category_slug=None):
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-created_at')

    # Если в адресе есть категория, фильтруем статьи
    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=current_category)

    return render(request, 'index.html', {
        'articles': articles, 
        'categories': categories,
        'current_category': current_category
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})