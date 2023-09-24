import datetime

from django.core.management import BaseCommand

from home2shopapp.models import Product


class Command(BaseCommand):
    help = 'Cоздаем товар'

    def add_arguments(self, parser):
        parser.add_argument('a', type=str, help='артикул')
        parser.add_argument('t', type=str, help='наименование')
        parser.add_argument('d', type=str, help='описание')
        parser.add_argument('up', type=float, help='цена')
        parser.add_argument('q', type=int, help='кол-во')
        parser.add_argument('is_v', type=bool, help='открыть доступ к товару?')

    def handle(self, *args, **options):
        obj = Product()
        obj.art = options['a']
        obj.title = options['t']
        obj.description = options['d']
        obj.unit_price = options['up']
        obj.qty = options['q']
        obj.is_visible = options['is_v']
        obj.save()
        self.stdout.write(str(obj))
