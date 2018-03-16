from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Answer, Message


def message_list(request):
    message = Message.objects.filter(created__lte=timezone.now()).order_by('msg_date')
    return render(request, 'ui_app/message_list.html', {})


def answer_list(request):
    answer = Answer.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'ui_app/answer_list.html', {'answer': answer})
