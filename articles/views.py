from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Article, Category, Review, Product

def home(request, category_slug=None):
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-created_at')
    reviews = Review.objects.all().order_by('-created_at')[:3]
    top_products = Product.objects.all().order_by('?')[:3] 

    query = request.GET.get('q') 
    if query:
        articles = articles.filter(
            Q(title__icontains=query) | 
            Q(text__icontains=query) | 
            Q(category__name__icontains=query)
        )

    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=current_category)

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            Review.objects.create(name=name, text=text)
            return redirect('home')
            
    return render(request, 'index.html', {
        'articles': articles, 
        'categories': categories,
        'reviews': reviews,
        'top_products': top_products, 
        'current_category': current_category,
        'query': query,
    })

# --- ВОТ ЗДЕСЬ МЫ ИЩЕМ ПОХОЖИЕ ТОВАРЫ ---
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Берем 3 случайных товара, которые НЕ принадлежат этой статье
    related_products = Product.objects.exclude(article=article).order_by('?')[:3]
    
    return render(request, 'article_detail.html', {
        'article': article,
        'related_products': related_products
    })

def add_like(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        article.likes += 1
        article.save()
        return JsonResponse({'likes': article.likes})
    return JsonResponse({'error': 'Ошибка'}, status=400)

def rate_article(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        rating = int(request.POST.get('rating', 0))
        article.rating = rating
        article.save()
        return JsonResponse({'success': True, 'rating': article.rating})
    return JsonResponse({'success': False}, status=400)