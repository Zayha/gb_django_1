import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView

from home2shopapp.models import Product
from .forms import MyModelForm, AddArticleForm, AddCommentForm
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
        return Article.objects.filter(author_id=author_id).order_by('-creation_time')


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
        context['comment_form'] = AddCommentForm()
        context['comments'] = Comment.objects.filter(article_id=pk).order_by('-creation_date')
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        article = Article.objects.get(pk=pk)
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return HttpResponseRedirect(self.request.path_info)  # Перенаправление на текущую страницу после отправки комментария
        else:
            # Если форма невалидна, вы можете обработать её в соответствии с вашими требованиями
            # Например, вы можете добавить обработку невалидной формы и возврат к статье.
            return self.render_to_response(self.get_context_data(form=form))


def success(request):
    return render(request, 'home2app/success.html', context={'url_home': reverse_lazy('home')})


# class NewAuthor(FormView):
#     template_name = 'home2app/new_author.html'
#     form_class = MyModelForm
#     success_url = reverse_lazy('success')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Добавить автора!'
#         return context


class NewAuthor(CreateView):
    model = Author
    template_name = 'home2app/new_author.html'
    form_class = MyModelForm
    success_url = reverse_lazy('success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить автора!'
        return context


class NewArticle(CreateView):
    model = Article
    template_name = 'home2app/new_author.html'
    form_class = AddArticleForm
    success_url = reverse_lazy('success')
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить статью'
        return context

# class AddComment(CreateView):
#     model = Comment
#     template_name = 'home2app/article_detail.html'
#     form_class = AddCommentForm
#     success_url = reverse_lazy('success')
#
#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset=queryset)
#         obj.view_count += 1
#         obj.save()
#         return obj
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         pk = self.kwargs.get('pk')
#         context['comments'] = Comment.objects.filter(article_id=pk).order_by('-creation_date')
#         return context



