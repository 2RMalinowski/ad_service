from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.answer_list, name='answer_list'),
]
