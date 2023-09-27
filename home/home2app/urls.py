from django.urls import path

from home2app.views import bin_choices, show_statistic, AuthorsWithArticlesListView, AuthorArticlesListView, \
    ArticleDetailView

urlpatterns = [
    path('h2/bc/', bin_choices, name='binc'),
    path('h2/shs/<int:n>', show_statistic, name='statistic'),
    path('l3/authors/', AuthorsWithArticlesListView.as_view(), name='authors'),
    path('l3/author/<int:author_id>/articles/', AuthorArticlesListView.as_view(), name='author-articles'),
    path('l3/article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
