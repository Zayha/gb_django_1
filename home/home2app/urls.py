from django.urls import path

from home2app.views import bin_choices, show_statistic

urlpatterns = [
    path('bc/', bin_choices, name='binc'),
    path('shs/<int:n>', show_statistic, name='statistic'),
]