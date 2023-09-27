import random

from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import HeadsOrTails, Article, Author, Comment


# Create your views here.

def bin_choices(request):
    result = random.choices([True, False])[0]
    db_obj = HeadsOrTails(result=result)
    db_obj.save()
    return HttpResponse(f'<h1>{"Орел" if result else "Решка"}</h1>')


def show_statistic(request, n):
    data = HeadsOrTails.statistic(n)
    print(data)
    return HttpResponse(f'{data["Orel"]=}\t,{data["Reshka"]=}\t, {data["n"]=}')


# отображаем всех авторов у которых есть стать
class AuthorsWithArticlesListView(ListView):
    model = Author
    template_name = 'home2app/authors_with_articles.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.filter(article__isnull=False).distinct()


class AuthorArticlesListView(ListView):
    model = Article
    template_name = 'home2app/author_articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Article.objects.filter(author_id=author_id).order_by('-creation_date')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'home2app/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        obj.view_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['comments'] = Comment.objects.filter(article_id=pk).order_by('-creation_date')
        return context
