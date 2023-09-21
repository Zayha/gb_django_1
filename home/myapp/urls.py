from django.urls import path

from myapp.views import index, bin_choices, dice, rand100, index2, lesson1, zero, about, index_wo_templates

urlpatterns = [
    path('', index, name='home'),
    path('ind/', index2, name='home2'),
    path('bin/', bin_choices, name='binch'),
    path('dice/', dice, name='dice'),
    path('rand100/', rand100, name='rand100'),
    path('lesson1/', lesson1, name='lesson1'),
    path('zero/', zero),
    path('about/', about, name='about'),
    path('home/', index_wo_templates, name='home3')

]
