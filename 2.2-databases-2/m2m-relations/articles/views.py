from django.shortcuts import render

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all()
    context = {
        'object_list': articles,
    }

    return render(request, template, context)
