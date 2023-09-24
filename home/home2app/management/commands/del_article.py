from django.core.management import BaseCommand

from home2app.models import Article


class Command(BaseCommand):
    help = 'Удаляем статью'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='id номер статьи'),

    def handle(self, *args, **options):
        art_id = options['id']

        obj_fot_del = Article.objects.filter(pk=art_id).first()
        if obj_fot_del:
            obj_fot_del.delete()
            self.stdout.write(f'Статья с id={art_id} удалена')
        else:
            self.stdout.write(f'Статья с id={art_id} отсутствует')
