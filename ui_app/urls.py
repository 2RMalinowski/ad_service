from django.urls import path
from . import views


urlpatterns = [
    path('', views.answer_list, name='answer_list'),
    path('', views.message_list, name='message_list'),
]
