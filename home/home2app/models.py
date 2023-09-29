from django.db import models

# Create your models here.
from django.urls import reverse


class HeadsOrTails(models.Model):
    result = models.BooleanField(verbose_name='Результаты броска')
    result_time = models.DateTimeField(auto_now_add=True, verbose_name='Время броска')

    @staticmethod
    def statistic(n):
        selected_data = HeadsOrTails.objects.all().order_by('-result_time')[:n]
        result = {'Orel': 0, 'Reshka': 0, 'n': len(selected_data)}
        for data in selected_data:
            if data.result:
                result['Orel'] += 1
            else:
                result['Reshka'] += 1
        return result


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    biography = models.TextField(verbose_name='Биография')
    b_date = models.DateField(verbose_name='Дата рождения')

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-articles', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержание статьи')
    published_date = models.DateField(verbose_name='Дата публикации')
    author = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, verbose_name='Категория')
    view_count = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована?')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Добавлена в базу')

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    author = models.ForeignKey('Author', verbose_name='Автор комментария', on_delete=models.DO_NOTHING)
    article = models.ForeignKey('Article', verbose_name='Статья', on_delete=models.DO_NOTHING)
    comment = models.TextField(verbose_name='Текст комментария')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.pk}\t{self.comment}'
