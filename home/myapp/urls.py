from django.urls import path

from myapp.views import Index, bin_choices, dice, rand100, index2, lesson1, zero, index_wo_templates, About, BinChoices, \
    Dice, Rand, FunkSelector

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('ind/', index2, name='home2'),
    path('bin/', bin_choices, name='binch'),
    path('dice/', dice, name='dice'),
    path('rand100/', rand100, name='rand100'),
    path('lesson1/', lesson1, name='lesson1'),
    path('zero/', zero),
    # path('about/', about, name='about'),
    path('about/', About.as_view(), name='about'),
    path('home/', index_wo_templates, name='home3'),
    path('l3/bin/<int:n>', BinChoices.as_view(), name='bin_l3'),
    path('l3/dice/<int:n>', Dice.as_view(), name='dice_l3'),
    path('l3/rand/<int:n>', Rand.as_view(), name='rand_l3'),
    path('l4/select/', FunkSelector.as_view(), name='select'),
]
