from django.urls import path
from .views import *

urlpatterns = [
    path('', question_form, name='question_form'),
    path('question_list/', question_list, name='question_list'),
]
