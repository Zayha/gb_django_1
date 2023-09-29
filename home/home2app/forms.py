from django import forms
from django.forms import DateInput


from .models import Author, Article, Comment


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Author  # Указываем модель, с которой связываем форму
        fields = '__all__'
        widgets = {
            'b_date': DateInput(attrs={'type': 'date'}),
        }


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'published_date', 'author', 'category']
        widgets = {
            'published_date': DateInput(attrs={'type': 'date'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']

    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        min_length=10,
        error_messages={
            'min_length': 'Комментарий должен содержать хотя бы 10 символов.'
        }
    )



