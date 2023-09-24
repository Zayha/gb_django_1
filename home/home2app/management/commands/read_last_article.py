from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from home2app.models import Article


class Command(BaseCommand):
    help = 'Read last article from db'

    def handle(self, *args, **options):
        try:
            article = Article.objects.all().latest('creation_time')
            self.stdout.write(article)
        except ObjectDoesNotExist:
            self.stdout.write('Нет записей в базе')

