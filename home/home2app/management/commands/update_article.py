from django.core.management import BaseCommand

from home2app.models import Article


class Command(BaseCommand):
    help = 'Редактируем текст статьи'

    def add_arguments(self, parser):
        parser.add_argument('desc', type=str, help='текст статьи')
        parser.add_argument('id', type=int, help='id номер статьи'),

    def handle(self, *args, **options):
        art_id = options['id']
        desc = options['desc']

        selected_object = Article.objects.filter(pk=art_id).first()
        if selected_object:
            selected_object.description = desc
            selected_object.save()
            self.stdout.write(f'Содержание статьи с id={art_id} изменено')
        else:
            self.stdout.write(f'id={art_id} не обнаружен')
