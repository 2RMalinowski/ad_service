from django.shortcuts import render, get_object_or_404
from .models import Answer, Message


def answer_list(request):
    answers = Answer.created.all()
    return render(request,
                  'ad_service/answer/list.html',
                  {'answers': answers})


