from django.shortcuts import render, get_object_or_404
from .models import Answer, Message


def message_list(request):
    return render(request, 'templates/ui_app/message_list.html', {})


def answer_list(request):
    return render(request, 'templates/ui_app/answer_list.html', {})
