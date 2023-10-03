from django.contrib import admin
from .models import Author, Article, HeadsOrTails, Comment


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'email', 'b_date']
    ordering = ['id', '-b_date']
    list_filter = ['last_name', 'b_date']
    list_editable = ['b_date']
    search_fields = ['last_name', 'biography']
    search_help_text = "Поиск по полям Фамилия и Биография"


class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]
    list_display_links = ['title']
    ordering = ['-creation_time']
    search_fields = ['title', 'description']
    search_help_text = "Поиск по полям Заголовок и Содержание статьи"
    list_editable = ['is_published']
    readonly_fields = ['creation_time', 'view_count']

    # fields = ['author', 'title', 'description', 'published_date', 'category', 'view_count', 'is_published',
    #           'creation_time']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Содержание',
            {
                'classes': ['collapse'],
                'fields': ['description']
            }
        ),
        (
            'Публикация',
            {
                'classes': ['wide'],
                'fields': ['author', 'category', 'published_date', 'is_published', 'creation_time']
            }
        ),
        (
            'Просмотры',
            {
                'classes': ['collapse'],
                'fields': ['view_count']
            }
        ),
    ]


admin.site.register(HeadsOrTails)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
