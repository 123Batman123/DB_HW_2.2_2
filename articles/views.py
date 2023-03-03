from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    obj = Article.objects.prefetch_related('tags')
    context = {'object_list': obj}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    #ordering = '-published_at'

    return render(request, template, context)
