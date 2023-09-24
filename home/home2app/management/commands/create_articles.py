import datetime
import random

from django.core.management import BaseCommand

from home2app.models import Article, Author


class Command(BaseCommand):
    help = 'Зоздаем фэйковые записи'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='Кол-во записей')

    def handle(self, *args, **options):
        n = options['n']
        today = datetime.date.today()
        for i in range(n):
            mix_day = random.randint(1, 10000)
            b_date = today - datetime.timedelta(days=mix_day)
            author = Author(
                name=f'Вася{i}',
                last_name='Васильев',
                email='123@321.ru',
                biography='нет ничего',
                b_date=b_date
            )
            author.save()
            Article(
                title=f'Это статья номер {n + 1}',
                description=f'Всякое описание статьи {n+1}',
                published_date=datetime.datetime.now(),
                author=author,
                category='Всякая ерунда',
            ).save()

